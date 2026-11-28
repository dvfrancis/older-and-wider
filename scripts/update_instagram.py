#!/usr/bin/env python3
"""Update the Instagram posts on message-board.html.

The script rewrites only the text between the marker comments in
message-board.html:

    <!-- instagram:posts:start -->
    ...
    <!-- instagram:posts:end -->

The script has two modes:

- API mode. The script uses this mode when IG_ACCESS_TOKEN and IG_USER_ID
  are set, or when --fixture is given. It gets the 10 latest posts from the
  Instagram API with Instagram Login (graph.instagram.com). It saves each
  photo as WebP width variants in assets/images/instagram/. It writes each
  post as static HTML with the photo. It never prints the token.
- List mode. The script uses this mode when the secrets are not set. It
  reads scripts/instagram-posts.txt and writes the 10 newest posts in the
  embed markup. message-board.js loads the embeds when the visitor asks.

Usage:

    python3 scripts/update_instagram.py                  update the page
    python3 scripts/update_instagram.py --check          show the diff, write nothing
    python3 scripts/update_instagram.py --fixture FILE   use a saved API response
    python3 scripts/update_instagram.py --refresh-token --token-out FILE
                                                         refresh the token

Exit codes:

    0  success (in --check mode: the page is up to date)
    1  --check only: the page would change
    2  error: the API, an image, the post list or the page is not usable.
       The page and the image folder do not change.

The script uses the Python standard library and the cwebp command only.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime
import difflib
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "message-board.html"
SITEMAP = ROOT / "sitemap.xml"
IMAGES = ROOT / "assets" / "images" / "instagram"
POST_LIST = ROOT / "scripts" / "instagram-posts.txt"
# The path of the image folder in the src of each img, relative to the page.
IMAGE_URL = "assets/images/instagram/"
PAGE_URL = "https://older-and-wider.dominicfrancis.co.uk/message-board.html"

API_HOST = "https://graph.instagram.com"
# Meta removes each Graph API version about two years after its release.
# Change this value before Meta removes it.
API_VERSION = "v27.0"
FIELDS = (
    "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp,alt_text,"
    "children{media_type,media_url,thumbnail_url}"
)

# The wall shows this number of posts.
POSTS = 10
# Get more posts than the wall shows, in case some are not usable.
FETCH = 20

# The widths of the WebP variants. The script does not make a variant
# that is wider than the original photo.
WIDTHS = (256, 480, 800, 1080)
WEBP_QUALITY = "80"
MAX_IMAGE_BYTES = 20 * 1024 * 1024

# The script downloads photos from these hosts only.
IMAGE_HOSTS = (".cdninstagram.com", ".fbcdn.net")

# Each post uses one of the three paper stocks, in this order.
STOCKS = ("post-red", "post-white", "post-letter")
# The number of columns that each post spans in the six-column wall
# from 48rem. This list must agree with the board rules in main.css.
SPANS = (4, 2, 3, 3, 2, 4, 3, 3, 2, 4)

KINDS = {
    "IMAGE": ("fa-camera", "Photo"),
    "CAROUSEL_ALBUM": ("fa-images", "Photo set"),
    "VIDEO": ("fa-video", "Video"),
}

EXCERPT = 90
ALT = 125

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

try:
    from zoneinfo import ZoneInfo

    LONDON = ZoneInfo("Europe/London")
except Exception:  # pragma: no cover - only without time zone data
    LONDON = datetime.timezone.utc

# Values that the script must never print. redact() removes them.
SECRETS: set[str] = set()
TOKEN_IN_TEXT = re.compile(r"(access_token=)[^&\s\"']+")


class FeedError(Exception):
    """The API, an image or the page cannot give a usable result."""


@dataclasses.dataclass
class Post:
    id: str
    kind: str
    caption: str
    alt_text: str
    permalink: str
    date: datetime.date
    image_url: str


@dataclasses.dataclass
class Image:
    stem: str
    variants: list[tuple[int, int, str]]  # (width, height, file name)


def redact(value: object) -> str:
    """Return the text with each secret and each access_token value removed."""
    result = str(value)
    for secret in SECRETS:
        if secret:
            result = result.replace(secret, "[hidden]")
    return TOKEN_IN_TEXT.sub(r"\1[hidden]", result)


# ---------------------------------------------------------------- API


def api_get(url: str) -> dict:
    """Return the JSON of a GET request. Raise FeedError with no secrets."""
    request = urllib.request.Request(url, headers={"User-Agent": "older-and-wider-instagram-update"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
    except urllib.error.HTTPError as error:
        detail = ""
        try:
            body = json.loads(error.read() or b"{}")
            detail = body.get("error", {}).get("message", "")
        except Exception:
            pass
        raise FeedError(redact(f"the API returned HTTP {error.code} {detail}".strip())) from None
    except Exception as error:
        raise FeedError(redact(f"cannot reach the API: {error}")) from None
    return parse_json(data)


def parse_json(data: bytes) -> dict:
    try:
        body = json.loads(data)
    except ValueError as error:
        raise FeedError(f"the API response is not JSON: {error}") from None
    if not isinstance(body, dict):
        raise FeedError("the API response is not a JSON object")
    if "error" in body:
        message = body["error"].get("message", "unknown error") if isinstance(body["error"], dict) else body["error"]
        raise FeedError(redact(f"the API returned an error: {message}"))
    return body


def media_url(user_id: str, token: str) -> str:
    query = urllib.parse.urlencode({"fields": FIELDS, "limit": FETCH, "access_token": token})
    return f"{API_HOST}/{API_VERSION}/{urllib.parse.quote(user_id)}/media?{query}"


def parse_timestamp(raw: str) -> datetime.date:
    """Return the UK calendar date of an API timestamp such as 2026-11-26T18:04:12+0000."""
    try:
        moment = datetime.datetime.strptime(raw, "%Y-%m-%dT%H:%M:%S%z")
    except (TypeError, ValueError):
        raise FeedError(f"cannot read the timestamp {raw!r}") from None
    return moment.astimezone(LONDON).date()


def cover_url(item: dict) -> str:
    """Return the URL of the photo that represents a post, or an empty string."""
    kind = item.get("media_type")
    if kind == "VIDEO":
        return item.get("thumbnail_url") or ""
    if kind == "CAROUSEL_ALBUM":
        children = (item.get("children") or {}).get("data") or []
        if children:
            first = children[0]
            if first.get("media_type") == "VIDEO":
                return first.get("thumbnail_url") or item.get("media_url") or ""
            return first.get("media_url") or item.get("media_url") or ""
    if kind in ("IMAGE", "CAROUSEL_ALBUM"):
        return item.get("media_url") or ""
    return ""


def parse_posts(body: dict) -> list[Post]:
    """Return the newest POSTS usable posts, newest first."""
    items = body.get("data")
    if not isinstance(items, list):
        raise FeedError("the API response has no data list")
    posts = []
    for item in items:
        if not isinstance(item, dict) or item.get("media_type") not in KINDS:
            continue
        post_id = str(item.get("id") or "")
        permalink = item.get("permalink") or ""
        image = cover_url(item)
        # Skip a post without a photo, for example a reel with no thumbnail.
        if not re.fullmatch(r"[0-9A-Za-z_]+", post_id) or not image:
            continue
        if not permalink.startswith("https://www.instagram.com/"):
            continue
        posts.append(
            Post(
                id=post_id,
                kind=item["media_type"],
                caption=str(item.get("caption") or ""),
                alt_text=str(item.get("alt_text") or ""),
                permalink=permalink,
                date=parse_timestamp(item.get("timestamp")),
                image_url=image,
            )
        )
    posts.sort(key=lambda post: post.date, reverse=True)
    if not posts:
        raise FeedError("the API returned no usable posts")
    return posts[:POSTS]


def refresh_token(token: str) -> tuple[str, int]:
    """Return a new long-lived token and its life in seconds."""
    query = urllib.parse.urlencode({"grant_type": "ig_refresh_token", "access_token": token})
    body = api_get(f"{API_HOST}/refresh_access_token?{query}")
    new = str(body.get("access_token") or "")
    if not re.fullmatch(r"[0-9A-Za-z_\-.|]{20,}", new):
        raise FeedError("the refresh response has no usable access_token")
    try:
        life = int(body.get("expires_in") or 0)
    except (TypeError, ValueError):
        life = 0
    return new, life


# ---------------------------------------------------------------- images


def check_image_url(url: str) -> None:
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    if parts.scheme != "https" or not host.endswith(IMAGE_HOSTS):
        raise FeedError(f"the photo is not on an Instagram host: {redact(parts.scheme)}://{host}")


def download(url: str, fixture_dir: Path | None) -> bytes:
    """Return the bytes of a photo. In fixture mode, read the file of the same name."""
    check_image_url(url)
    try:
        if fixture_dir is not None:
            name = Path(urllib.parse.urlsplit(url).path).name
            data = (fixture_dir / "images" / name).read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "older-and-wider-instagram-update"})
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read(MAX_IMAGE_BYTES + 1)
    except Exception as error:
        raise FeedError(redact(f"cannot download a photo: {error}")) from None
    if not data or len(data) > MAX_IMAGE_BYTES:
        raise FeedError("a photo is empty or too large")
    return data


def webp_size(path: Path) -> tuple[int, int]:
    """Return the width and height of a WebP file from its header."""
    data = path.read_bytes()[:30]
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise FeedError(f"{path.name} is not a WebP file")
    chunk = data[12:16]
    if chunk == b"VP8 ":
        width = int.from_bytes(data[26:28], "little") & 0x3FFF
        height = int.from_bytes(data[28:30], "little") & 0x3FFF
    elif chunk == b"VP8L":
        bits = int.from_bytes(data[21:25], "little")
        width = (bits & 0x3FFF) + 1
        height = ((bits >> 14) & 0x3FFF) + 1
    elif chunk == b"VP8X":
        width = int.from_bytes(data[24:27], "little") + 1
        height = int.from_bytes(data[27:30], "little") + 1
    else:
        raise FeedError(f"{path.name} has an unknown WebP format")
    return width, height


def cwebp(source: Path, target: Path, width: int | None) -> None:
    command = ["cwebp", "-quiet", "-q", WEBP_QUALITY, "-metadata", "none"]
    if width:
        command += ["-resize", str(width), "0"]
    command += [str(source), "-o", str(target)]
    try:
        subprocess.run(command, check=True, capture_output=True, timeout=120)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as error:
        raise FeedError(f"cwebp cannot convert a photo: {error}") from None


def make_variants(post: Post, data: bytes, work: Path) -> Image:
    """Write the WebP variants of one photo to the work folder."""
    # The name contains the post ID and a hash of the photo. A changed photo
    # gets a new name, because the site caches images for one year.
    stem = f"{post.id}-{hashlib.sha256(data).hexdigest()[:10]}"
    source = work / f"{stem}.source"
    source.write_bytes(data)
    full = work / f"{stem}.full.webp"
    cwebp(source, full, None)
    original_width, _ = webp_size(full)
    widths = [w for w in WIDTHS if w < original_width]
    widths.append(min(original_width, WIDTHS[-1]))
    variants = []
    for width in widths:
        name = f"{stem}_{width}.webp"
        target = work / name
        if width == original_width:
            shutil.copyfile(full, target)
        else:
            cwebp(source, target, width)
        real_width, real_height = webp_size(target)
        variants.append((real_width, real_height, name))
    source.unlink()
    full.unlink()
    return Image(stem=stem, variants=variants)


# ---------------------------------------------------------------- page


def text(value: str) -> str:
    return html.escape(value, quote=False)


def attr(value: str) -> str:
    return html.escape(value, quote=True)


def short_date(day: datetime.date) -> str:
    return f"{day.day} {MONTHS[day.month - 1][:3]} {day.year}"


def long_date(day: datetime.date) -> str:
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


def first_line(caption: str) -> str:
    """Return the first line of a caption without the hashtags at its end."""
    for line in caption.splitlines():
        line = re.sub(r"(\s*#\w+)+\s*$", "", line)
        line = " ".join(line.split())
        if line and not line.startswith("#"):
            return line
    return ""


def shorten(value: str, limit: int) -> str:
    """Cut a text at a word boundary and add an ellipsis if it is too long."""
    if len(value) <= limit:
        return value
    cut = value[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,.;:-")
    return f"{cut}…"


def sizes(index: int) -> str:
    """Return the sizes value for the post at this position on the wall.

    On phones a post is the full width less the gutters and the padding.
    From 48rem a post spans SPANS[index] of six columns with 2rem gaps.
    The content is at most 80rem wide.
    """
    span = SPANS[index % len(SPANS)]
    widest = span * 11 + (span - 1) * 2 - 2.5
    vw = round(span * 100 / 6, 2)
    offset = round(span * 14 / 6 - (span - 1) * 2 + 2.5, 2)
    return (
        f"(min-width: 80rem) {widest:g}rem, "
        f"(min-width: 48rem) calc({vw:g}vw - {offset:g}rem), "
        "calc(100vw - 4.5rem)"
    )


def render_posts(posts: list[Post], images: dict[str, Image]) -> list[str]:
    """Return the lines of the posts list, without indentation."""
    lines = ['<ul class="board-list">']
    for index, post in enumerate(posts):
        image = images[post.id]
        icon, label = KINDS[post.kind]
        stock = STOCKS[index % len(STOCKS)]
        opening = first_line(post.caption)
        alt = shorten(" ".join(post.alt_text.split()) or opening, ALT) or (
            f"An Older and Wider Instagram post from {long_date(post.date)}"
        )
        width, height, largest = image.variants[-1]
        srcset = ", ".join(f"{IMAGE_URL}{name} {w}w" for w, _, name in image.variants)
        excerpt = (
            f'<span class="post-text"><q>{text(shorten(opening, EXCERPT))}</q></span>'
            if opening
            else '<span class="post-text">A new post on Instagram</span>'
        )
        item = [
            "<li>",
            f'    <a class="board-post {stock}" href="{attr(post.permalink)}" rel="external noopener" target="_blank" aria-describedby="new-tab">',
            '        <span class="post-photo">',
            f'            <img src="{IMAGE_URL}{largest}" srcset="{srcset}"',
            f'                sizes="{sizes(index)}" width="{width}" height="{height}"',
            f'                loading="lazy" decoding="async" alt="{attr(alt)}">',
            "        </span>",
            f'        <span class="post-meta"><i class="fa-solid {icon}" aria-hidden="true"></i>{label}',
            f'            <time datetime="{post.date.isoformat()}">{short_date(post.date)}</time></span>',
            f"        {excerpt}",
            '        <span class="post-link">See this post on Instagram</span>',
            "    </a>",
            "</li>",
        ]
        lines += [f"    {line}" for line in item]
    lines.append("</ul>")
    return lines


# ---------------------------------------------------------------- post list


@dataclasses.dataclass
class ListedPost:
    date: datetime.date
    url: str
    text: str
    kind: str


LIST_URL = re.compile(r"https://www\.instagram\.com/(?P<type>p|reel)/[A-Za-z0-9_-]+/")
LIST_KINDS = {"photo": "IMAGE", "photo set": "CAROUSEL_ALBUM", "video": "VIDEO"}


def read_post_list(path: Path) -> list[ListedPost]:
    """Return the newest POSTS posts of the post list, newest first.

    Each line is "date | URL | text", with an optional fourth field
    "photo", "photo set" or "video". A line that starts with # is a comment.
    A bad line stops the script, and the message gives its line number.
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise FeedError(f"cannot read the post list: {error}") from None
    posts = []
    for number, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        where = f"{path.name} line {number}"
        fields = [field.strip() for field in line.split("|")]
        if len(fields) not in (3, 4):
            raise FeedError(f"{where} must have 3 or 4 parts with | between them")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields[0]):
            raise FeedError(f"{where}: {fields[0]!r} is not a date such as 2026-11-27")
        try:
            day = datetime.date.fromisoformat(fields[0])
        except ValueError:
            raise FeedError(f"{where}: {fields[0]!r} is not a real date") from None
        url = fields[1]
        # A link from the Share button of Instagram has a query, for example
        # ?igsh=abc. Remove the query and the fragment. Use the www address.
        url = url.split("#", 1)[0].split("?", 1)[0]
        if url.startswith("https://instagram.com/"):
            url = "https://www." + url[len("https://"):]
        if url.startswith("https://www.instagram.com/") and not url.endswith("/"):
            url += "/"
        match = LIST_URL.fullmatch(url)
        if not match:
            raise FeedError(
                f"{where}: {fields[1]!r} is not an Instagram post address such as "
                "https://www.instagram.com/p/POSTID/"
            )
        words = " ".join(fields[2].split())
        if not words or words in ('""', "“”"):
            raise FeedError(f"{where} has no text")
        if len(fields) == 4:
            kind = LIST_KINDS.get(fields[3].lower())
            if kind is None:
                raise FeedError(f"{where}: the fourth part must be photo, photo set or video")
        else:
            kind = "VIDEO" if match.group("type") == "reel" else "IMAGE"
        posts.append(ListedPost(date=day, url=url, text=words, kind=kind))
    if not posts:
        raise FeedError(f"{path.name} has no posts")
    # The sort keeps the file order for posts on the same day.
    posts.sort(key=lambda post: post.date, reverse=True)
    return posts[:POSTS]


def render_list(posts: list[ListedPost]) -> list[str]:
    """Return the lines of the posts list in the embed markup, without indentation.

    message-board.js turns each blockquote into an Instagram embed when the
    visitor asks. Without JavaScript, each post is a link to Instagram.
    """
    lines = ['<ul class="board-list">']
    for index, post in enumerate(posts):
        icon, label = KINDS[post.kind]
        stock = STOCKS[index % len(STOCKS)]
        words = post.text
        if len(words) > 2 and words[0] == '"' and words[-1] == '"':
            body = f"<q>{text(words[1:-1].strip())}</q>"
        else:
            body = text(words)
        item = [
            "<li>",
            f'    <blockquote class="instagram-media {stock}"',
            f'        data-instgrm-permalink="{attr(post.url)}"',
            '        data-instgrm-version="14">',
            f'        <a href="{attr(post.url)}" rel="external noopener" target="_blank" aria-describedby="new-tab">',
            f'            <span class="post-meta"><i class="fa-solid {icon}" aria-hidden="true"></i>{label}',
            f'                <time datetime="{post.date.isoformat()}">{short_date(post.date)}</time></span>',
            f'            <span class="post-text">{body}</span>',
            '            <span class="post-link">See this post on Instagram</span>',
            "        </a>",
            "    </blockquote>",
            "</li>",
        ]
        lines += [f"    {line}" for line in item]
    lines.append("</ul>")
    return lines


# ---------------------------------------------------------------- output


MARKERS = re.compile(
    r"^(?P<indent>[ \t]*)<!-- instagram:posts:start -->\n"
    r"(?P<body>.*?)"
    r"^[ \t]*<!-- instagram:posts:end -->$",
    re.DOTALL | re.MULTILINE,
)


def apply_posts(page: str, lines: list[str]) -> str:
    """Replace the text between the markers. Keep the indentation."""
    matches = list(MARKERS.finditer(page))
    if len(matches) != 1:
        raise FeedError("the page must have one pair of instagram:posts markers")
    match = matches[0]
    indent = match.group("indent")
    body = "".join(f"{indent}{line}\n" for line in lines)
    return page[: match.start("body")] + body + page[match.end("body") :]


def update_sitemap(sitemap: str, day: datetime.date) -> str:
    """Set the lastmod date of the message board in the sitemap."""
    pattern = re.compile(rf"(<loc>{re.escape(PAGE_URL)}</loc>\s*<lastmod>)[0-9-]+(</lastmod>)")
    new, count = pattern.subn(rf"\g<1>{day.isoformat()}\g<2>", sitemap)
    if count != 1:
        raise FeedError("sitemap.xml must have one lastmod for the message board")
    return new


def today() -> datetime.date:
    return datetime.datetime.now(LONDON).date()


def write_atomic(path: Path, content: str) -> None:
    handle, temp = tempfile.mkstemp(dir=path.parent, prefix=".instagram-", suffix=".tmp")
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


# ---------------------------------------------------------------- main


def run_refresh(token_out: str | None) -> int:
    token = os.environ.get("IG_ACCESS_TOKEN", "")
    SECRETS.add(token)
    if not token:
        print("error: IG_ACCESS_TOKEN is not set.", file=sys.stderr)
        return 2
    if not token_out:
        print("error: --refresh-token needs --token-out FILE.", file=sys.stderr)
        return 2
    try:
        new, life = refresh_token(token)
    except FeedError as error:
        print(f"error: {redact(error)}. The token is not changed.", file=sys.stderr)
        return 2
    SECRETS.add(new)
    # Mask the new token in the job log before anything else.
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::add-mask::{new}", flush=True)
    path = Path(token_out)
    handle = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(handle, "w", encoding="utf-8") as stream:
        stream.write(new)
    print(f"Refreshed the token. It expires in {life // 86400} days.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--fixture", help="saved API response (JSON) to use in place of the API")
    parser.add_argument("--posts", default=str(POST_LIST), help="post list for list mode (default: scripts/instagram-posts.txt)")
    parser.add_argument("--page", default=str(PAGE), help="page to update (default: message-board.html)")
    parser.add_argument("--images", default=str(IMAGES), help="image folder (default: assets/images/instagram)")
    parser.add_argument("--sitemap", default=str(SITEMAP), help="sitemap to update (default: sitemap.xml)")
    parser.add_argument("--check", action="store_true", help="print the diff and exit 1 if the page would change")
    parser.add_argument("--refresh-token", action="store_true", help="refresh the access token, then stop")
    parser.add_argument("--token-out", help="file for the new token (with --refresh-token)")
    args = parser.parse_args(argv)

    if args.refresh_token:
        return run_refresh(args.token_out)

    page_path = Path(args.page)
    images_dir = Path(args.images)
    sitemap_path = Path(args.sitemap)
    token = os.environ.get("IG_ACCESS_TOKEN", "")
    user_id = os.environ.get("IG_USER_ID", "")
    SECRETS.add(token)
    # API mode needs both secrets, or a fixture. Otherwise the script uses
    # the post list, and the file is the only source.
    mode = "api" if args.fixture or (token and user_id) else "list"
    work = Path(tempfile.mkdtemp(prefix="instagram-"))
    try:
        images: dict[str, Image] = {}
        if mode == "list":
            posts = read_post_list(Path(args.posts))
            lines = render_list(posts)
        else:
            if shutil.which("cwebp") is None:
                raise FeedError("the cwebp command is not installed (install the webp package)")
            if args.fixture:
                fixture = Path(args.fixture)
                fixture_dir = fixture.parent
                try:
                    body = parse_json(fixture.read_bytes())
                except OSError as error:
                    raise FeedError(f"cannot read the fixture: {error}") from None
            else:
                fixture_dir = None
                body = api_get(media_url(user_id, token))
            posts = parse_posts(body)
            images = {post.id: make_variants(post, download(post.image_url, fixture_dir), work) for post in posts}
            lines = render_posts(posts, images)
        old = page_path.read_text(encoding="utf-8")
        new = apply_posts(old, lines)
        old_sitemap = sitemap_path.read_text(encoding="utf-8")
        new_sitemap = update_sitemap(old_sitemap, today())
    except (FeedError, OSError) as error:
        shutil.rmtree(work, ignore_errors=True)
        print(f"error: {redact(error)}. {page_path.name} is not changed.", file=sys.stderr)
        return 2

    wanted = {name for image in images.values() for _, _, name in image.variants}
    present = {path.name for path in images_dir.glob("*.webp")} if images_dir.is_dir() else set()
    changed = new != old or wanted != present
    try:
        if args.check:
            if changed:
                sys.stdout.writelines(
                    difflib.unified_diff(
                        old.splitlines(keepends=True),
                        new.splitlines(keepends=True),
                        fromfile=f"{page_path.name} (now)",
                        tofile=f"{page_path.name} (from Instagram)",
                    )
                )
                for name in sorted(wanted - present):
                    print(f"+ image {name}")
                for name in sorted(present - wanted):
                    print(f"- image {name}")
                return 1
            print(f"{page_path.name} is up to date ({len(posts)} posts, {mode} mode).")
            return 0

        if changed:
            # Add the new photos first, then the page, then remove the old
            # photos. The live page never points at a missing file.
            if wanted - present:
                images_dir.mkdir(parents=True, exist_ok=True)
            added = []
            try:
                for name in sorted(wanted - present):
                    shutil.copyfile(work / name, images_dir / name)
                    added.append(images_dir / name)
                write_atomic(page_path, new)
            except BaseException:
                for path in added:
                    path.unlink(missing_ok=True)
                raise
            if new_sitemap != old_sitemap:
                write_atomic(sitemap_path, new_sitemap)
            for name in sorted(present - wanted):
                (images_dir / name).unlink()
            print(f"Updated {page_path.name} with {len(posts)} posts ({mode} mode).")
        else:
            print(f"{page_path.name} is up to date ({len(posts)} posts, {mode} mode). No change.")
        github_output(changed=str(changed).lower(), posts=len(posts), mode=mode)
        return 0
    except OSError as error:
        print(f"error: {redact(error)}.", file=sys.stderr)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
