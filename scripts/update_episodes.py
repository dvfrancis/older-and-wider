#!/usr/bin/env python3
"""Update the episode sections of index.html from the podcast RSS feed.

The script reads the Acast feed and rewrites only the text between the
episode marker comments in index.html, for example:

    <!-- episodes:masthead:start -->
    ...
    <!-- episodes:masthead:end -->

Usage:

    python3 scripts/update_episodes.py                 update index.html
    python3 scripts/update_episodes.py --check         show the diff, write nothing
    python3 scripts/update_episodes.py --feed FILE     use a local feed file

Exit codes:

    0  success (in --check mode: the page is up to date)
    1  --check only: the page would change
    2  error: the feed did not load or parse, or the data is not usable.
       The page does not change.

The script uses the Python standard library only.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime
import difflib
import email.utils
import html
import os
import re
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FEED_URL = "https://feeds.acast.com/public/shows/63b6b30a19c20a0011527ce4"
SHOW_URL = "https://shows.acast.com/older-and-wider-podcast"
PAGE = Path(__file__).resolve().parent.parent / "index.html"

ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"

# The ticket shows the 15 episodes before the latest one.
TICKET_SIZE = 15
# The newest episodes on the ticket carry a dab and fill the "Last called" list.
CALLED = 4
# The latest episode plus the ticket.
NEEDED = TICKET_SIZE + 1

# The 15 numbered cells of the 9 x 3 bingo ticket, in document order.
# The numbers go up column by column, as on a UK bingo ticket. Each row has
# five numbers and four blanks. The blanks are fixed in index.html and are
# not generated. Do not change this list without the blanks.
TICKET_CELLS = [
    (1, 1), (3, 1),
    (2, 2),
    (1, 3), (2, 3),
    (2, 4), (3, 4),
    (1, 5),
    (2, 6), (3, 6),
    (1, 7),
    (1, 8), (3, 8),
    (2, 9), (3, 9),
]

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# "Ep 374. Title", "Ep. 366 Title", "Ep 124.Title", "Episode 12: Title", "374. Title"
TITLE_NUMBER = re.compile(
    r"^\s*(?:ep(?:isode)?\.?\s*(?P<a>\d+)|(?P<b>\d+)\s*[.:])\s*[.:\-]?\s*",
    re.IGNORECASE,
)

try:
    from zoneinfo import ZoneInfo

    LONDON = ZoneInfo("Europe/London")
except Exception:  # pragma: no cover - only without time zone data
    LONDON = datetime.timezone.utc


class FeedError(Exception):
    """The feed cannot give the data that the page needs."""


@dataclasses.dataclass
class Episode:
    number: int
    title: str
    date: datetime.date
    duration: str
    url: str


# ---------------------------------------------------------------- feed


def load_feed(source: str) -> bytes:
    """Return the raw feed from a URL or a local file."""
    try:
        if re.match(r"^https?://", source):
            request = urllib.request.Request(
                source, headers={"User-Agent": "older-and-wider-episode-update"}
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        return Path(source).read_bytes()
    except Exception as error:
        raise FeedError(f"cannot load the feed {source}: {error}") from error


def parse_number(item: ET.Element, title: str) -> int | None:
    """Return the episode number from itunes:episode, or from the title."""
    field = (item.findtext(f"{ITUNES}episode") or "").strip()
    if field.isdigit():
        return int(field)
    match = TITLE_NUMBER.match(title)
    if match:
        return int(match.group("a") or match.group("b"))
    return None


def clean_title(title: str) -> str:
    """Remove the number prefix and extra white space from a title."""
    title = TITLE_NUMBER.sub("", title, count=1)
    return " ".join(title.split())


def format_duration(raw: str) -> str:
    """Return a duration as m:ss, or h:mm:ss for one hour or more."""
    raw = raw.strip()
    parts = raw.split(":")
    if not raw or len(parts) > 3 or not all(p.isdigit() for p in parts):
        raise FeedError(f"cannot read the duration {raw!r}")
    seconds = 0
    for part in parts:
        seconds = seconds * 60 + int(part)
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def parse_moment(raw: str) -> datetime.datetime:
    """Return an RFC 822 pubDate as an aware datetime."""
    try:
        moment = email.utils.parsedate_to_datetime(raw.strip())
    except (TypeError, ValueError) as error:
        raise FeedError(f"cannot read the date {raw!r}") from error
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=datetime.timezone.utc)
    return moment


def parse_date(raw: str) -> datetime.date:
    """Return the UK calendar date of an RFC 822 pubDate."""
    return parse_moment(raw).astimezone(LONDON).date()


def parse_feed(data: bytes) -> list[Episode]:
    """Return the latest NEEDED episodes, newest first.

    The newest item must have an episode number. Older items without a
    number (for example a "sick note" week) are not episodes and are skipped.
    """
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise FeedError(f"cannot parse the feed: {error}") from error
    channel = root.find("channel")
    if channel is None:
        raise FeedError("the feed has no channel")

    items = []
    for item in channel.findall("item"):
        kind = (item.findtext(f"{ITUNES}episodeType") or "full").strip().lower()
        if kind != "full":
            continue
        raw_title = item.findtext("title") or ""
        pub_date = item.findtext("pubDate")
        if not raw_title.strip() or not pub_date:
            raise FeedError("an item has no title or no pubDate")
        items.append((parse_moment(pub_date), item, raw_title))
    if not items:
        raise FeedError("the feed has no episodes")
    items.sort(key=lambda entry: entry[0], reverse=True)

    episodes: list[Episode] = []
    for position, (_, item, raw_title) in enumerate(items):
        number = parse_number(item, raw_title)
        if number is None:
            if position == 0:
                raise FeedError(f"the newest item has no episode number: {raw_title.strip()!r}")
            continue
        url = (item.findtext("link") or "").strip()
        if not re.match(r"^https://", url):
            url = SHOW_URL
        episodes.append(
            Episode(
                number=number,
                title=clean_title(raw_title),
                date=parse_date(item.findtext("pubDate") or ""),
                duration=format_duration(item.findtext(f"{ITUNES}duration") or ""),
                url=url,
            )
        )
        if len(episodes) == NEEDED:
            break

    if len(episodes) < NEEDED:
        raise FeedError(f"the feed has {len(episodes)} numbered episodes, {NEEDED} are needed")
    numbers = [episode.number for episode in episodes]
    if any(newer <= older for newer, older in zip(numbers, numbers[1:])):
        raise FeedError(f"the episode numbers do not go down with the dates: {numbers}")
    return episodes


# ---------------------------------------------------------------- page


def text(value: str) -> str:
    return html.escape(value, quote=False)


def attr(value: str) -> str:
    return html.escape(value, quote=True)


def long_date(day: datetime.date) -> str:
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


def short_date(day: datetime.date) -> str:
    return f"{day.day} {MONTHS[day.month - 1][:3]} {day.year}"


def render_sections(episodes: list[Episode]) -> dict[str, list[str]]:
    """Return the lines for each marked section, without indentation."""
    latest = episodes[0]
    ticket = sorted(episodes[1:NEEDED], key=lambda episode: episode.number)
    called = ticket[-CALLED:]

    def meta(episode: Episode, css: str) -> str:
        return (
            f'<span class="{css}"><time datetime="{episode.date.isoformat()}">'
            f"{short_date(episode.date)}</time>, {episode.duration}</span>"
        )

    sections = {
        "masthead": [
            f'<span>Issue {latest.number} <span aria-hidden="true">·</span> '
            f"{long_date(latest.date)}</span>",
        ],
        "cover": [
            '<a class="slab slab-lead" href="#listen">',
            f'    <span class="lead-title">{text(latest.title)}</span>',
            '    <span class="lead-action">',
            '        <span class="play-disc" aria-hidden="true"><i class="fa-solid fa-play"></i></span>',
            "        Play the latest episode",
            f'        <span class="lead-time">{latest.duration}</span>',
            "    </span>",
            "</a>",
        ],
        "this-week": [
            '<p class="listen-ep">',
            f'    <span class="ep-no">{latest.number}</span>',
            f'    <span class="ep-title">{text(latest.title)}</span>',
            f"    {meta(latest, 'ep-meta')}",
            "</p>",
        ],
        "ticket-serial": [
            '<p class="ticket-serial"><span>Older and Wider</span> '
            f"<span>Ticket {latest.number}</span></p>",
        ],
        "ticket": [],
        "last-called": [],
    }
    for (row, column), episode in zip(TICKET_CELLS, ticket):
        dab = " called" if episode in called else ""
        sections["ticket"].append(
            f'<li class="tk r{row} c{column}{dab}"><a href="{attr(episode.url)}" rel="external">'
            f'<span class="visually-hidden">Episode </span>{episode.number}</a></li>'
        )
    for episode in reversed(called):
        sections["last-called"] += [
            "<li>",
            f'    <a href="{attr(episode.url)}" rel="external">',
            f'        <span class="lc-no">{episode.number}</span>',
            f'        <span class="lc-title">{text(episode.title)}</span>',
            f"        {meta(episode, 'lc-meta')}",
            "    </a>",
            "</li>",
        ]
    return sections


def apply_sections(page: str, sections: dict[str, list[str]]) -> str:
    """Replace the text between each pair of markers. Keep the indentation."""
    for name, lines in sections.items():
        pattern = re.compile(
            rf"^(?P<indent>[ \t]*)<!-- episodes:{re.escape(name)}:start -->\n"
            rf"(?P<body>.*?)"
            rf"^(?P<end>[ \t]*<!-- episodes:{re.escape(name)}:end -->)$",
            re.DOTALL | re.MULTILINE,
        )
        matches = list(pattern.finditer(page))
        if len(matches) != 1:
            raise FeedError(f"index.html must have one pair of markers for {name!r}")
        match = matches[0]
        indent = match.group("indent")
        body = "".join(f"{indent}{line}\n" for line in lines)
        page = page[: match.start("body")] + body + page[match.end("body") :]
    return page


def write_atomic(path: Path, content: str) -> None:
    handle, temp = tempfile.mkstemp(dir=path.parent, prefix=".index-", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="") as stream:
            stream.write(content)
        os.chmod(temp, path.stat().st_mode & 0o777)
        os.replace(temp, path)
    except BaseException:
        if os.path.exists(temp):
            os.unlink(temp)
        raise


def github_output(**values: object) -> None:
    """Write step outputs when the script runs in GitHub Actions."""
    target = os.environ.get("GITHUB_OUTPUT")
    if not target:
        return
    with open(target, "a", encoding="utf-8") as stream:
        for key, value in values.items():
            stream.write(f"{key}={value}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--feed", default=FEED_URL, help="feed URL or local file (default: the Acast feed)")
    parser.add_argument("--page", default=str(PAGE), help="page to update (default: index.html)")
    parser.add_argument("--check", action="store_true", help="print the diff and exit 1 if the page would change")
    args = parser.parse_args(argv)

    page_path = Path(args.page)
    try:
        episodes = parse_feed(load_feed(args.feed))
        old = page_path.read_text(encoding="utf-8")
        new = apply_sections(old, render_sections(episodes))
    except (FeedError, OSError) as error:
        print(f"error: {error}. index.html is not changed.", file=sys.stderr)
        return 2

    latest = episodes[0].number
    changed = new != old
    if args.check:
        if changed:
            sys.stdout.writelines(
                difflib.unified_diff(
                    old.splitlines(keepends=True),
                    new.splitlines(keepends=True),
                    fromfile=f"{page_path.name} (now)",
                    tofile=f"{page_path.name} (from the feed)",
                )
            )
            return 1
        print(f"{page_path.name} is up to date (episode {latest}).")
        return 0

    if changed:
        write_atomic(page_path, new)
        print(f"Updated {page_path.name} for episode {latest}.")
    else:
        print(f"{page_path.name} is up to date (episode {latest}). No change.")
    github_output(changed=str(changed).lower(), episode=latest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
