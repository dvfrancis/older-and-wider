"""Build the list of all venues on archive.html.

The script reads every show row in the archive tables, and every show on
live-shows.html. It merges the names that refer to the same venue, counts the
shows at each venue and groups the venues by town. It then writes the list
between these markers in archive.html:

    <!-- venues:list:start -->
    <!-- venues:list:end -->

Three data files in scripts/ add to the list:

    venue-links.txt          the website of each venue
    venue-places.txt         the county and the position of each town
    venue-map-outline.txt    the coastline for the map

Each town must have a line in venue-places.txt, or the script stops.

Usage, from the repository root:

    python3 scripts/update_archive_venues.py --check   # show the diff, write nothing
    python3 scripts/update_archive_venues.py           # update archive.html

Exit codes: 0 no change or change written, 1 change found in --check mode,
2 error (archive.html is not changed).
"""

import argparse
import difflib
import html
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "archive.html"
SHOWS_PAGE = ROOT / "live-shows.html"
LINKS = ROOT / "scripts" / "venue-links.txt"
PLACES = ROOT / "scripts" / "venue-places.txt"
OUTLINE = ROOT / "scripts" / "venue-map-outline.txt"

# The map shows this box: longitude -11 to 2.2, latitude 49 to 61.
MAP_WEST, MAP_EAST, MAP_SOUTH, MAP_NORTH = -11.0, 2.2, 49.0, 61.0
MAP_SCALE = 40
MAP_STRETCH = math.cos(math.radians(55))

NEW_TAB = 'rel="external noopener" target="_blank" aria-describedby="new-tab"'

START = "<!-- venues:list:start -->"
END = "<!-- venues:list:end -->"

# Rows with these venue names do not name a venue.
SKIP = {"Venue uncertain"}

# Town names that refer to the same place.
TOWN_ALIASES = {
    "Bexhill": "Bexhill-on-Sea",
    "Chiswick": "London",
    "Melbourne": "Melbourne, Australia",
    "Sydney": "Sydney, Australia",
    "Brisbane": "Brisbane, Australia",
}

# Venues in a town that has the same name as a town in another country.
TOWN_BY_VENUE = {
    ("Burswood Theatre", "Perth"): "Perth, Australia",
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
    ("Birmingham Rep, The Studio", "Birmingham"): "Birmingham Rep",
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


def live_show_rows(page):
    """Return (venue, town) for each show on live-shows.html."""
    rows = []
    for item in re.findall(r'<li class="show">(.*?)</li>', page, re.S):
        town = re.search(r'<h3 class="show-place">(.*?)</h3>', item, re.S)
        venue = re.search(r'<p class="show-venue">(.*?)</p>', item, re.S)
        if not town or not venue:
            raise VenueError("a show on live-shows.html has no town or no venue")
        rows.append((text(venue.group(1)), text(town.group(1))))
    return rows


def read_links(source):
    """Return {(venue, town): url} from the text of venue-links.txt."""
    links = {}
    for number, line in enumerate(source.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 3 or not parts[2].startswith("https://"):
            raise VenueError(f"venue-links.txt line {number} must be 'Town | Venue | https://...'")
        town, venue, url = parts
        links[(venue, town)] = url
    return links


def read_places(source):
    """Return {town: (area, latitude, longitude)} from the text of venue-places.txt."""
    places = {}
    for number, line in enumerate(source.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split("|")]
        try:
            town, area, lat, lon = parts
            places[town] = (area, float(lat), float(lon))
        except ValueError:
            raise VenueError(f"venue-places.txt line {number} must be 'Town | Area | latitude | longitude'")
    return places


def read_outline(source):
    """Return a list of rings of (longitude, latitude) from venue-map-outline.txt."""
    rings = []
    for number, line in enumerate(source.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            ring = [(float(lon), float(lat)) for lon, lat in (point.split(",") for point in line.split())]
        except ValueError:
            raise VenueError(f"venue-map-outline.txt line {number} must be 'longitude,latitude' pairs")
        rings.append(ring)
    return rings


def project(lon, lat):
    """Return the (x, y) position on the map for a longitude and a latitude."""
    x = (lon - MAP_WEST) * MAP_STRETCH * MAP_SCALE
    y = (MAP_NORTH - lat) * MAP_SCALE
    return round(x, 1), round(y, 1)


def on_map(lat, lon):
    return MAP_SOUTH <= lat <= MAP_NORTH and MAP_WEST <= lon <= MAP_EAST


def join_names(names):
    """Return "A", "A and B" or "A, B and C"."""
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def town_id(town):
    return "arc-venue-town-" + re.sub(r"[^a-z0-9]+", "-", town.casefold()).strip("-")


def render_map(towns, places, outline, pad):
    """Return the lines of the SVG map, with one dot for each town on the map."""
    width, _ = project(MAP_EAST, MAP_SOUTH)
    _, height = project(MAP_WEST, MAP_SOUTH)
    land = " ".join(
        "M" + " L".join(f"{x},{y}" for x, y in (project(lon, lat) for lon, lat in ring)) + " Z" for ring in outline
    )
    dots = []
    for town, venues in towns.items():
        area, lat, lon = places[town]
        if not on_map(lat, lon):
            continue
        shows = sum(number for _, number in venues)
        x, y = project(lon, lat)
        radius = round(min(2.5 + math.sqrt(shows) * 0.9, 9), 1)
        dots.append((radius, town, x, y, shows))
    # Draw the big dots first, so the small dots stay on top and visible.
    dots.sort(key=lambda dot: (-dot[0], dot[1]))
    out = [
        f'{pad}<figure class="arc-venue-map">',
        f'{pad}    <svg class="arc-venue-map-svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="arc-venue-map-title">',
        f'{pad}        <title id="arc-venue-map-title">Map of the venue towns in the UK, Ireland and the Channel Islands. '
        f"A bigger dot means more shows.</title>",
        f'{pad}        <path class="arc-venue-map-land" d="{land}"/>',
        f'{pad}        <g class="arc-venue-map-dots">',
    ]
    for radius, town, x, y, shows in dots:
        label = html.escape(f"{town}, {plural(shows, 'show')}", quote=False)
        out.append(
            f'{pad}            <circle cx="{x}" cy="{y}" r="{radius}" data-town="{town_id(town)}"><title>{label}</title></circle>'
        )
    away = [town for town in towns if not on_map(*places[town][1:])]
    out.append(f"{pad}        </g>")
    out.append(f"{pad}    </svg>")
    credit = (
        f'Town positions © <a href="https://www.openstreetmap.org/copyright" {NEW_TAB}>OpenStreetMap contributors</a>. '
        f'Coastline from <a href="https://www.naturalearthdata.com/" {NEW_TAB}>Natural Earth</a>.'
    )
    caption = ""
    if away:
        # Group the towns by country, for example "Perth and Sydney in Australia".
        countries = {}
        for town in away:
            name, _, country = town.rpartition(", ")
            countries.setdefault(country, []).append(name or country)
        groups = [f"{join_names(names)} in {country}" for country, names in countries.items()]
        caption = html.escape(f"Not on the map: {join_names(groups)}. ", quote=False)
    out.append(f'{pad}    <figcaption class="arc-venue-map-caption">{caption}{credit}</figcaption>')
    out.append(f"{pad}</figure>")
    return out


def normalise(venue, town):
    """Return the (venue, town) to show for one row."""
    town = TOWN_ALIASES.get(town, town)
    # Remove notes in brackets, for example "(warm-up)" or "(matinee)".
    venue = re.sub(r"\s*\([^)]*\)$", "", venue).strip()
    town = TOWN_BY_VENUE.get((venue, town), town)
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


def plural(number, word):
    return f"{number} {word}" if number == 1 else f"{number} {word}s"


def render(venues, links=None, places=None, outline=None):
    """Return the markup that goes between the markers."""
    links = links or {}
    places = places or {}
    shows = sum(number for _, number in venues)
    towns = {}
    for (venue, town), number in venues:
        towns.setdefault(town, []).append((venue, number))
    letters = {}
    for town in towns:
        letters.setdefault(town[0].upper(), []).append(town)
    missing = [town for town in towns if town not in places]
    if places and missing:
        raise VenueError(f"venue-places.txt has no line for: {', '.join(missing)}")
    ids = Counter(town_id(town) for town in towns)
    clashes = [town for town in towns if ids[town_id(town)] > 1]
    if clashes:
        raise VenueError(f"these towns get the same id: {', '.join(clashes)}")

    pad = " " * 28
    out = [
        f'{pad}<details class="arc-tour" id="all-venues">',
        f'{pad}    <summary><span class="arc-tour-name">All venues</span> <span class="arc-tour-meta">'
        f"{len(venues)} venues in {len(towns)} towns and cities, {shows} shows</span></summary>",
        f'{pad}    <div class="arc-venue-search" id="arc-venue-search" hidden>',
        f'{pad}        <label class="arc-venue-search-label" for="arc-venue-search-input">Search for a town, a county or a venue</label>',
        f'{pad}        <input class="arc-venue-search-input" id="arc-venue-search-input" type="search" autocomplete="off">',
        f'{pad}        <p class="arc-venue-search-status" id="arc-venue-search-status" aria-live="polite"></p>',
        f"{pad}    </div>",
        f'{pad}    <div class="arc-venue-browser">',
    ]
    if places and outline:
        out += render_map(towns, places, outline, pad + "        ")
    out += [f'{pad}        <div class="arc-venue-letters">']
    inner = pad + "    "
    for letter, names in letters.items():
        count = sum(len(towns[name]) for name in names)
        out.append(f'{inner}        <details class="arc-venue-letter">')
        out.append(
            f'{inner}            <summary><span class="arc-venue-letter-name">{letter}</span> '
            f'<span class="arc-venue-letter-meta">{plural(len(names), "town")}, {plural(count, "venue")}</span></summary>'
        )
        out.append(f'{inner}            <ul class="arc-venue-towns">')
        for name in names:
            area = f' <span class="arc-venue-county">{html.escape(places[name][0], quote=False)}</span>' if name in places else ""
            out.append(f'{inner}                <li class="arc-venue-town" id="{town_id(name)}">')
            out.append(f'{inner}                    <p class="arc-venue-town-name">{html.escape(name, quote=False)}{area}</p>')
            out.append(f'{inner}                    <ul class="arc-venue-names">')
            for venue, number in towns[name]:
                label = html.escape(venue, quote=False)
                url = links.get((venue, name))
                if url:
                    label = f'<a href="{html.escape(url)}" {NEW_TAB}>{label}</a>'
                out.append(
                    f'{inner}                        <li>{label} <span class="arc-venue-count">{plural(number, "show")}</span></li>'
                )
            out.append(f"{inner}                    </ul>")
            out.append(f"{inner}                </li>")
        out.append(f"{inner}            </ul>")
        out.append(f"{inner}        </details>")
    out.append(f"{pad}        </div>")
    out.append(f"{pad}    </div>")
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
    parser.add_argument("--shows", type=Path, default=SHOWS_PAGE, help="the live shows page")
    parser.add_argument("--links", type=Path, default=LINKS, help="the file of venue links")
    parser.add_argument("--places", type=Path, default=PLACES, help="the file of town areas and positions")
    parser.add_argument("--outline", type=Path, default=OUTLINE, help="the coastline for the map")
    args = parser.parse_args(argv)
    try:
        old = args.page.read_text(encoding="utf-8")
        rows = show_rows(old) + live_show_rows(args.shows.read_text(encoding="utf-8"))
        links = read_links(args.links.read_text(encoding="utf-8")) if args.links.exists() else {}
        places = read_places(args.places.read_text(encoding="utf-8")) if args.places.exists() else {}
        outline = read_outline(args.outline.read_text(encoding="utf-8")) if args.outline.exists() else []
        new = apply(old, render(count_venues(rows), links, places, outline))
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
