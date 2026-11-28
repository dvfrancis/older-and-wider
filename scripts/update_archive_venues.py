"""Build the list of all venues on archive.html.

The script reads every show row in the archive tables. It merges the names
that refer to the same venue, counts the shows at each venue, and writes a
table between these markers in archive.html:

    <!-- venues:list:start -->
    <!-- venues:list:end -->

Usage, from the repository root:

    python3 scripts/update_archive_venues.py --check   # show the diff, write nothing
    python3 scripts/update_archive_venues.py           # update archive.html

Exit codes: 0 no change or change written, 1 change found in --check mode,
2 error (archive.html is not changed).
"""

import argparse
import difflib
import html
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "archive.html"

START = "<!-- venues:list:start -->"
END = "<!-- venues:list:end -->"

# Rows with these venue names do not name a venue.
SKIP = {"Venue uncertain"}

# Town names that refer to the same place.
TOWN_ALIASES = {
    "Bexhill": "Bexhill-on-Sea",
    "Chiswick": "London",
    "Melbourne, Australia": "Melbourne",
}

# Venue names that refer to the same venue, keyed by (venue, town) after the
# town aliases and the removal of notes in brackets. The value is the name
# to show.
VENUE_ALIASES = {
    ("Her Majesty's Theatre", "Aberdeen"): "His Majesty's Theatre",
    ("The Mill Arts Centre", "Banbury"): "Mill Arts Centre",
    ("The Broadway", "Barking"): "Broadway Theatre",
    ("Anvil Arts", "Basingstoke"): "The Anvil",
    ("Civic Halls", "Bedworth"): "Civic Hall",
    ("Civic Theatre", "Bedworth"): "Civic Hall",
    ("MAC", "Belfast"): "The MAC",
    ("New Alexandra Theatre", "Birmingham"): "Alexandra Theatre",
    ("Albert Halls", "Bolton"): "The Albert Halls",
    ("Pavilion Ballroom", "Bournemouth"): "Pavilion",
    ("Arts Theatre", "Braintree"): "Braintree Arts Theatre",
    ("Braintree Arts Centre", "Braintree"): "Braintree Arts Theatre",
    ("Gulbenkian", "Canterbury"): "The Gulbenkian",
    ("Gulbenkian Theatre", "Canterbury"): "The Gulbenkian",
    ("Civic Cramphorn Studio", "Chelmsford"): "Cramphorn Theatre",
    ("Tabard Theatre", "London"): "Theatre at the Tabard",
    ("The Tabard", "London"): "Theatre at the Tabard",
    ("Arts Centre", "Colchester"): "Colchester Arts Centre",
    ("Ashcroft Theatre, Fairfield Halls", "Croydon"): "Fairfield Halls",
    ("Fairfield Halls, Studio", "Croydon"): "Fairfield Halls",
    ("The Orchard", "Dartford"): "Orchard Theatre",
    ("The Gardyne", "Dundee"): "Gardyne Theatre",
    ("The Harlington", "Fleet"): "Harlington Theatre",
    ("Quarter House", "Folkestone"): "Quarterhouse",
    ("Courtyard Theatre", "Hereford"): "The Courtyard",
    ("Wolsey Theatre", "Ipswich"): "New Wolsey Theatre",
    ("Brewery Arts", "Kendal"): "Brewery Arts Centre",
    ("Arts Centre Guildhall", "King's Lynn"): "Arts Centre",
    ("Lancaster Grand", "Lancaster"): "Grand Theatre",
    ("Royal Spa Centre Studio", "Leamington Spa"): "Royal Spa Centre",
    ("Leicester Y Theatre", "Leicester"): "Y Theatre",
    ("New Theatre Royal", "Lincoln"): "Theatre Royal",
    ("The Concert Room, St George's Hall", "Liverpool"): "St George's Hall",
    ("Millfield Arts Centre", "London"): "Millfield Theatre",
    ("Queen Elizabeth Hall, Southbank Centre", "London"): "Southbank Centre",
    ("Masham Town Hall", "Masham"): "Town Hall",
    ("Stable Theatre", "Milton Keynes"): "The Stables",
    ("Stables Theatre", "Milton Keynes"): "The Stables",
    ("The Brunton", "Musselburgh"): "Brunton Theatre",
    ("Derngate", "Northampton"): "Royal and Derngate",
    ("Royal Theatre", "Northampton"): "Royal and Derngate",
    ("Coliseum Theatre", "Oldham"): "Oldham Coliseum",
    ("Coliseum", "Oldham"): "Oldham Coliseum",
    ("Broadway", "Peterborough"): "Broadway Theatre",
    ("Cresset Theatre", "Peterborough"): "The Cresset",
    ("Arts Centre", "Pontardawe"): "Pontardawe Arts Centre",
    ("Hexagon Theatre", "Reading"): "The Hexagon",
    ("The Lowry, Quays Theatre", "Salford"): "The Lowry",
    ("Atkinson Theatre", "Southport"): "The Atkinson",
    ("Stafford Gatehouse Theatre", "Stafford"): "Gatehouse Theatre",
    ("Regents Theatre", "Stoke-on-Trent"): "Regent Theatre",
    ("Assembly Theatre", "Tunbridge Wells"): "Assembly Hall Theatre",
    ("Huntingdon Halls", "Worcester"): "Huntingdon Hall",
}


class VenueError(Exception):
    """The archive page cannot be read or updated."""


def text(cell):
    """Return the visible text of a table cell."""
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", cell)).split())


def show_rows(page):
    """Return (venue, town) for each show row outside the venue list."""
    if page.count(START) != 1 or page.count(END) != 1:
        raise VenueError("archive.html must have one pair of venue markers")
    before, rest = page.split(START)
    after = rest.split(END)[1]
    rows = []
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", before + after, re.S):
        cells = [text(cell) for cell in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        if len(cells) == 4:
            # Older and Wider live: date, show, venue, town.
            rows.append((cells[2], cells[3]))
        elif len(cells) == 3:
            # Tour dates: date, town, venue.
            rows.append((cells[2], cells[1]))
        elif cells:
            raise VenueError(f"a show row has {len(cells)} cells: {cells}")
    if not rows:
        raise VenueError("archive.html has no show rows")
    return rows


def normalise(venue, town):
    """Return the (venue, town) to show for one row."""
    town = TOWN_ALIASES.get(town, town)
    # Remove notes in brackets, for example "(warm-up)" or "(matinee)".
    venue = re.sub(r"\s*\([^)]*\)$", "", venue).strip()
    venue = VENUE_ALIASES.get((venue, town), venue)
    return venue, town


def sort_key(item):
    (venue, town), _ = item
    name = re.sub(r"^The ", "", venue)
    return (town.casefold(), name.casefold())


def count_venues(rows):
    """Return a sorted list of ((venue, town), number of shows)."""
    counts = Counter(normalise(venue, town) for venue, town in rows if venue not in SKIP)
    return sorted(counts.items(), key=sort_key)


def render(venues):
    """Return the markup that goes between the markers."""
    shows = sum(number for _, number in venues)
    pad = " " * 28
    out = [
        f'{pad}<details class="arc-tour" id="all-venues">',
        f'{pad}    <summary><span class="arc-tour-name">All venues</span> <span class="arc-tour-meta">'
        f"{len(venues)} venues, {shows} shows</span></summary>",
        f'{pad}    <table class="arc-dates arc-venues">',
        f'{pad}        <caption class="visually-hidden">All venues, by town or city</caption>',
        f"{pad}        <thead>",
        f"{pad}            <tr>",
        f'{pad}                <th scope="col">Town or city</th>',
        f'{pad}                <th scope="col">Venue</th>',
        f'{pad}                <th scope="col">Shows</th>',
        f"{pad}            </tr>",
        f"{pad}        </thead>",
    ]
    letter = None
    for (venue, town), number in venues:
        first = town[0].upper()
        if first != letter:
            if letter is not None:
                out.append(f"{pad}        </tbody>")
            out.append(f"{pad}        <tbody>")
            out.append(f'{pad}            <tr class="arc-year">')
            out.append(f'{pad}                <th colspan="3" scope="rowgroup">{first}</th>')
            out.append(f"{pad}            </tr>")
            letter = first
        word = "show" if number == 1 else "shows"
        out.append(f"{pad}            <tr>")
        out.append(f'{pad}                <td class="arc-town">{html.escape(town, quote=False)}</td>')
        out.append(f"{pad}                <td>{html.escape(venue, quote=False)}</td>")
        out.append(f'{pad}                <td class="arc-count">{number} {word}</td>')
        out.append(f"{pad}            </tr>")
    out.append(f"{pad}        </tbody>")
    out.append(f"{pad}    </table>")
    out.append(f"{pad}</details>")
    return "\n".join(out) + "\n"


def apply(page, block):
    """Return the page with the block between the markers."""
    pattern = re.compile(re.escape(START) + r"\n.*?" + r"([ \t]*)" + re.escape(END), re.S)
    match = pattern.search(page)
    if not match:
        raise VenueError("the venue markers are not on their own lines")
    indent = match.group(1)
    return page[: match.start()] + START + "\n" + block + indent + END + page[match.end():]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="show the diff and write nothing")
    parser.add_argument("--page", type=Path, default=PAGE, help="the archive page")
    args = parser.parse_args(argv)
    try:
        old = args.page.read_text(encoding="utf-8")
        new = apply(old, render(count_venues(show_rows(old))))
    except (OSError, VenueError) as error:
        print(f"Error: {error}. archive.html is not changed.", file=sys.stderr)
        return 2
    if new == old:
        print("The venue list is up to date.")
        return 0
    if args.check:
        sys.stdout.writelines(
            difflib.unified_diff(old.splitlines(True), new.splitlines(True), "archive.html", "archive.html (new)")
        )
        return 1
    args.page.write_text(new, encoding="utf-8")
    print("The venue list is updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
