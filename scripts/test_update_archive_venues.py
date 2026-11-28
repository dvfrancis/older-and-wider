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
</table>
            <!-- venues:list:start -->
            <!-- venues:list:end -->
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

    def tearDown(self):
        shutil.rmtree(self.tmp)


class LivePageTest(unittest.TestCase):
    def test_live_list_is_up_to_date(self):
        # Run the script after each change to the show tables of archive.html.
        page = LIVE_PAGE.read_text(encoding="utf-8")
        block = venues.render(venues.count_venues(venues.show_rows(page)))
        self.assertEqual(venues.apply(page, block), page)

    def test_every_show_row_is_counted(self):
        page = LIVE_PAGE.read_text(encoding="utf-8")
        rows = venues.show_rows(page)
        listed = venues.count_venues(rows)
        skipped = sum(1 for venue, _ in rows if venue in venues.SKIP)
        self.assertEqual(sum(number for _, number in listed), len(rows) - skipped)


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
            ],
        )

    def test_check_finds_a_change_and_writes_nothing(self):
        code, out, _ = run("--check", "--page", str(self.page))
        self.assertEqual(code, 1)
        self.assertIn("+", out)
        self.assertEqual(self.page.read_text(encoding="utf-8"), SMALL_PAGE)

    def test_update_writes_the_list_once(self):
        code, _, _ = run("--page", str(self.page))
        self.assertEqual(code, 0)
        html = self.page.read_text(encoding="utf-8")
        self.assertIn('<span class="arc-tour-meta">3 venues, 4 shows</span>', html)
        self.assertIn('<td class="arc-count">2 shows</td>', html)
        self.assertIn('<td class="arc-count">1 show</td>', html)
        self.assertNotIn("Venue uncertain</td>\n", html.split(venues.START)[1])
        # A second run changes nothing.
        code, out, _ = run("--check", "--page", str(self.page))
        self.assertEqual(code, 0, out)

    def test_text_outside_the_markers_is_unchanged(self):
        run("--page", str(self.page))
        html = self.page.read_text(encoding="utf-8")
        self.assertEqual(html.split(venues.START)[0], SMALL_PAGE.split(venues.START)[0])

    def test_names_are_escaped(self):
        page = SMALL_PAGE.replace("Leicester Square Theatre", "Bar &amp; Grill")
        block = venues.render(venues.count_venues(venues.show_rows(page)))
        self.assertIn("<td>Bar &amp; Grill</td>", block)


class BadPageTest(PageTestCase):
    def test_page_without_markers(self):
        self.page.write_text("<p>No markers</p>\n", encoding="utf-8")
        code, _, err = run("--page", str(self.page))
        self.assertEqual(code, 2)
        self.assertIn("not changed", err)
        self.assertEqual(self.page.read_text(encoding="utf-8"), "<p>No markers</p>\n")

    def test_missing_page(self):
        code, _, err = run("--page", str(self.page))
        self.assertEqual(code, 2)
        self.assertIn("not changed", err)


if __name__ == "__main__":
    unittest.main()
