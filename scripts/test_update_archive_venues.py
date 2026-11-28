"""Tests for update_archive_venues.py.

Run from the repository root:

    python3 -m unittest discover -s scripts -v

The tests do not change archive.html. They use temporary copies.
"""

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import update_archive_venues as venues  # noqa: E402

LIVE_PAGE = HERE.parent / "archive.html"

SMALL_PAGE = """<table>
<tr>
<td class="arc-date"><time datetime="2025-12-21">Sunday 21 December 2025</time></td>
<td>Older and Wider Live at Christmas</td>
<td>Leicester Square Theatre</td>
<td>London</td>
</tr>
<tr>
<td class="arc-date">2023</td>
<td>Work in progress</td>
<td>Venue uncertain</td>
<td>Uncertain</td>
</tr>
</table>
<table>
<tr class="arc-year"><th colspan="3" scope="rowgroup">2014</th></tr>
<tr>
<td class="arc-date"><time datetime="2014-03-01">Sat 1 Mar 2014</time></td>
<td class="arc-town">Chiswick</td>
<td>The Tabard (warm-up)</td>
</tr>
<tr>
<td class="arc-date"><time datetime="2014-03-02">Sun 2 Mar 2014</time></td>
<td class="arc-town">Aberdeen</td>
<td>Her Majesty's Theatre</td>
</tr>
<tr>
<td class="arc-date"><time datetime="2024-03-02">Sat 2 Mar 2024</time></td>
<td class="arc-town">Aberdeen</td>
<td>His Majesty's Theatre</td>
</tr>
<tr>
<td class="arc-date"><time datetime="2009-05-02">Sat 2 May 2009</time></td>
<td class="arc-town">Perth</td>
<td>Burswood Theatre</td>
</tr>
</table>
            <!-- venues:list:start -->
            <!-- venues:list:end -->
"""

SMALL_SHOWS = """<ul>
<li class="show">
<h3 class="show-place">Aberdeen</h3>
<p class="show-venue">Music Hall</p>
</li>
</ul>
"""

SMALL_LINKS = """# Comment
Aberdeen | Music Hall | https://example.com/music-hall?a=1&b=2
"""

SMALL_PLACES = """# Comment
Aberdeen | Aberdeen City | 57.1482 | -2.0928
London | Greater London | 51.5074 | -0.1278
Perth, Australia | Western Australia | -31.9523 | 115.8613
"""

SMALL_OUTLINE = """# Comment
-3,50 -2,50 -2,51 -3,51 -3,50
"""


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = venues.main(list(args))
    return code, out.getvalue(), err.getvalue()


class PageTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.page = self.tmp / "archive.html"
        self.files = {}
        for name, text in {
            "shows": SMALL_SHOWS,
            "links": SMALL_LINKS,
            "places": SMALL_PLACES,
            "outline": SMALL_OUTLINE,
        }.items():
            path = self.tmp / f"{name}.txt"
            path.write_text(text, encoding="utf-8")
            self.files[name] = path

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_script(self, *args):
        options = []
        for name, path in self.files.items():
            options += [f"--{name}", str(path)]
        return run(*args, "--page", str(self.page), *options)


class LivePageTest(unittest.TestCase):
    def test_live_list_is_up_to_date(self):
        # Run the script after each change to the show tables or the data files.
        code, out, err = run("--check")
        self.assertEqual(code, 0, out + err)

    def test_every_show_row_is_counted(self):
        page = LIVE_PAGE.read_text(encoding="utf-8")
        rows = venues.show_rows(page) + venues.live_show_rows(venues.SHOWS_PAGE.read_text(encoding="utf-8"))
        listed = venues.count_venues(rows)
        skipped = sum(1 for venue, _ in rows if venue in venues.SKIP)
        self.assertEqual(sum(number for _, number in listed), len(rows) - skipped)

    def test_every_link_matches_a_venue(self):
        # A link with a wrong town or venue name never shows on the page.
        page = LIVE_PAGE.read_text(encoding="utf-8")
        rows = venues.show_rows(page) + venues.live_show_rows(venues.SHOWS_PAGE.read_text(encoding="utf-8"))
        listed = {key for key, _ in venues.count_venues(rows)}
        links = venues.read_links(venues.LINKS.read_text(encoding="utf-8"))
        self.assertEqual(sorted(set(links) - listed), [])

    def test_every_town_has_a_place(self):
        page = LIVE_PAGE.read_text(encoding="utf-8")
        rows = venues.show_rows(page) + venues.live_show_rows(venues.SHOWS_PAGE.read_text(encoding="utf-8"))
        towns = {town for (_, town), _ in venues.count_venues(rows)}
        places = venues.read_places(venues.PLACES.read_text(encoding="utf-8"))
        self.assertEqual(sorted(towns - set(places)), [])


class SmallPageTest(PageTestCase):
    def setUp(self):
        super().setUp()
        self.page.write_text(SMALL_PAGE, encoding="utf-8")

    def test_names_are_merged(self):
        listed = venues.count_venues(venues.show_rows(SMALL_PAGE))
        self.assertEqual(
            listed,
            [
                (("His Majesty's Theatre", "Aberdeen"), 2),
                (("Leicester Square Theatre", "London"), 1),
                (("Theatre at the Tabard", "London"), 1),
                (("Burswood Theatre", "Perth, Australia"), 1),
            ],
        )

    def test_check_finds_a_change_and_writes_nothing(self):
        code, out, _ = self.run_script("--check")
        self.assertEqual(code, 1)
        self.assertIn("+", out)
        self.assertEqual(self.page.read_text(encoding="utf-8"), SMALL_PAGE)

    def test_update_writes_the_list_once(self):
        code, _, err = self.run_script()
        self.assertEqual(code, 0, err)
        html = self.page.read_text(encoding="utf-8")
        self.assertIn("5 venues in 3 towns and cities, 6 shows", html)
        self.assertIn('<span class="arc-venue-count">2 shows</span>', html)
        self.assertIn('<span class="arc-venue-count">1 show</span>', html)
        self.assertNotIn("Venue uncertain", html.split(venues.START)[1])
        # A second run changes nothing.
        code, out, _ = self.run_script("--check")
        self.assertEqual(code, 0, out)

    def test_towns_are_grouped_by_letter(self):
        self.run_script()
        html = self.page.read_text(encoding="utf-8")
        self.assertIn('<span class="arc-venue-letter-name">A</span>', html)
        self.assertIn('<span class="arc-venue-letter-meta">1 town, 2 venues</span>', html)
        self.assertIn('<span class="arc-venue-letter-meta">1 town, 2 venues</span>', html.split("arc-venue-letter-name\">L")[1])
        self.assertEqual(html.count('<li class="arc-venue-town"'), 3)

    def test_link_is_escaped_and_opens_in_a_new_tab(self):
        self.run_script()
        html = self.page.read_text(encoding="utf-8")
        self.assertIn(
            f'<a href="https://example.com/music-hall?a=1&amp;b=2" {venues.NEW_TAB}>Music Hall</a>',
            html,
        )

    def test_county_shows_next_to_the_town(self):
        self.run_script()
        html = self.page.read_text(encoding="utf-8")
        self.assertIn(
            '<p class="arc-venue-town-name">Aberdeen <span class="arc-venue-county">Aberdeen City</span></p>', html
        )

    def test_map_has_a_dot_for_each_town_on_the_map(self):
        self.run_script()
        html = self.page.read_text(encoding="utf-8")
        self.assertEqual(html.count("<circle "), 2)
        self.assertIn('data-town="arc-venue-town-aberdeen"><title>Aberdeen, 3 shows</title>', html)
        self.assertIn("Not on the map: Perth in Australia.", html)
        self.assertIn("OpenStreetMap contributors", html)

    def test_list_without_data_files_has_no_map(self):
        code, _, err = run(
            "--page", str(self.page), "--shows", str(self.files["shows"]),
            "--links", str(self.tmp / "none"), "--places", str(self.tmp / "none"), "--outline", str(self.tmp / "none"),
        )
        self.assertEqual(code, 0, err)
        html = self.page.read_text(encoding="utf-8")
        self.assertNotIn("<svg", html)
        self.assertIn('<li class="arc-venue-town"', html)

    def test_text_outside_the_markers_is_unchanged(self):
        self.run_script()
        html = self.page.read_text(encoding="utf-8")
        self.assertEqual(html.split(venues.START)[0], SMALL_PAGE.split(venues.START)[0])

    def test_names_are_escaped(self):
        page = SMALL_PAGE.replace("Leicester Square Theatre", "Bar &amp; Grill")
        block = venues.render(venues.count_venues(venues.show_rows(page)))
        self.assertIn("<li>Bar &amp; Grill <span", block)


class BadDataTest(PageTestCase):
    def setUp(self):
        super().setUp()
        self.page.write_text(SMALL_PAGE, encoding="utf-8")

    def assert_error(self, name, text, message):
        self.files[name].write_text(text, encoding="utf-8")
        code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn(message, err)
        self.assertEqual(self.page.read_text(encoding="utf-8"), SMALL_PAGE)

    def test_town_without_a_place(self):
        self.assert_error("places", SMALL_PLACES.replace("London |", "Londres |"), "no line for: London")

    def test_bad_place_line(self):
        self.assert_error("places", SMALL_PLACES + "Bath | Somerset | north\n", "venue-places.txt line 5")

    def test_bad_link_line(self):
        self.assert_error("links", SMALL_LINKS + "Bath | Theatre Royal | http://example.com\n", "venue-links.txt line 3")

    def test_bad_outline_line(self):
        self.assert_error("outline", SMALL_OUTLINE + "1,2 3\n", "venue-map-outline.txt line 3")

    def test_towns_with_the_same_id(self):
        rows = [("Hall", "St Ives"), ("Hall", "St. Ives")]
        with self.assertRaises(venues.VenueError):
            venues.render(venues.count_venues(rows))

    def test_show_without_a_venue(self):
        self.assert_error("shows", '<li class="show"><h3 class="show-place">Bath</h3></li>', "no town or no venue")


class BadPageTest(PageTestCase):
    def test_page_without_markers(self):
        self.page.write_text("<p>No markers</p>\n", encoding="utf-8")
        code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn("not changed", err)
        self.assertEqual(self.page.read_text(encoding="utf-8"), "<p>No markers</p>\n")

    def test_missing_page(self):
        code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn("not changed", err)


if __name__ == "__main__":
    unittest.main()
