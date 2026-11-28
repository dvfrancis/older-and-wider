"""Tests for update_episodes.py.

Run from the repository root:

    python3 -m unittest discover -s scripts -v

The tests use the feeds in scripts/fixtures/ and a temporary copy of
scripts/fixtures/index.html. That file is a copy of index.html at episode 374,
so the tests still pass after the live page moves on. The tests do not use
the network and do not change index.html.
"""

import contextlib
import io
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import update_episodes  # noqa: E402

FIXTURES = HERE / "fixtures"
PAGE = FIXTURES / "index.html"
LIVE_PAGE = HERE.parent / "index.html"
SHOW = "https://shows.acast.com/older-and-wider-podcast/episodes/"


class PageTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.page = self.tmp / "index.html"
        shutil.copyfile(PAGE, self.page)
        self.before = self.page.read_bytes()
        self.sitemap = self.tmp / "sitemap.xml"
        shutil.copyfile(HERE.parent / "sitemap.xml", self.sitemap)
        self.sitemap_before = self.sitemap.read_bytes()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_script(self, feed, *extra):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = update_episodes.main(
                ["--feed", str(FIXTURES / feed), "--page", str(self.page),
                 "--sitemap", str(self.sitemap), *extra]
            )
        return code, out.getvalue(), err.getvalue()

    def section(self, name):
        html = self.page.read_text(encoding="utf-8")
        match = re.search(
            rf"<!-- episodes:{name}:start -->\n(.*?)<!-- episodes:{name}:end -->", html, re.S
        )
        self.assertIsNotNone(match, f"no markers for {name}")
        return match.group(1)


class CurrentFeedTest(PageTestCase):
    """(a) The current feed gives no change."""

    def test_check_reports_no_change(self):
        code, out, _ = self.run_script("feed-current.xml", "--check")
        self.assertEqual(code, 0, out)

    def test_update_writes_nothing_new(self):
        code, _, _ = self.run_script("feed-current.xml")
        self.assertEqual(code, 0)
        self.assertEqual(self.page.read_bytes(), self.before)
        self.assertEqual(self.sitemap.read_bytes(), self.sitemap_before)


class NewEpisodeTest(PageTestCase):
    """(b) A new episode 375 updates every part of the page."""

    def setUp(self):
        super().setUp()
        self.code, self.out, self.err = self.run_script("feed-new-episode.xml")

    def test_exit_code(self):
        self.assertEqual(self.code, 0, self.err)
        self.assertIn("episode 375", self.out)

    def test_sitemap_lastmod(self):
        sitemap = self.sitemap.read_text(encoding="utf-8")
        day = update_episodes.parse_feed((FIXTURES / "feed-new-episode.xml").read_bytes())[0].date
        self.assertIn(
            f"<loc>{update_episodes.HOME_URL}</loc>\n    <lastmod>{day.isoformat()}</lastmod>",
            sitemap,
        )

    def test_check_mode_writes_nothing(self):
        shutil.copyfile(PAGE, self.page)
        code, out, _ = self.run_script("feed-new-episode.xml", "--check")
        self.assertEqual(code, 1)
        self.assertIn("+", out)
        self.assertEqual(self.page.read_bytes(), self.before)

    def test_masthead(self):
        self.assertIn(
            '<span>Issue 375 <span aria-hidden="true">·</span> 4 December 2026</span>',
            self.section("masthead"),
        )

    def test_cover(self):
        cover = self.section("cover")
        self.assertIn(
            '<span class="lead-title">The one with the mince pies &amp; a &lt;surprise&gt; guest</span>',
            cover,
        )
        self.assertIn('<span class="lead-time">1:02:03</span>', cover)

    def test_this_week(self):
        week = self.section("this-week")
        self.assertIn('<span class="ep-no">375</span>', week)
        self.assertIn("mince pies &amp; a &lt;surprise&gt; guest", week)
        self.assertIn('<time datetime="2026-12-04">4 Dec 2026</time>, 1:02:03', week)

    def test_ticket(self):
        self.assertIn("<span>Ticket 375</span>", self.section("ticket-serial"))
        ticket = self.section("ticket")
        cells = re.findall(r'<li class="tk (r\d c\d)( called)?"><a href="([^"]+)"[^>]*>.*?</span>(\d+)</a>', ticket)
        self.assertEqual([int(c[3]) for c in cells], list(range(360, 375)))
        self.assertEqual([int(c[3]) for c in cells if c[1]], [371, 372, 373, 374])
        positions = [cell[0] for cell in cells]
        expected = [f"r{r} c{c}" for r, c in update_episodes.TICKET_CELLS]
        self.assertEqual(positions, expected)
        self.assertTrue(all(c[2].startswith(SHOW) for c in cells))
        self.assertEqual(len({c[2] for c in cells}), 15)

    def test_links_open_in_a_new_tab(self):
        for name in ("ticket", "last-called"):
            links = re.findall(r"<a [^>]*>", self.section(name))
            self.assertTrue(links)
            for link in links:
                self.assertIn('rel="external noopener" target="_blank" aria-describedby="new-tab"', link)

    def test_ticket_rows_have_five_numbers(self):
        rows = re.findall(r'class="tk r(\d)', self.section("ticket"))
        self.assertEqual(sorted(rows), ["1"] * 5 + ["2"] * 5 + ["3"] * 5)

    def test_last_called(self):
        called = self.section("last-called")
        self.assertEqual(re.findall(r'<span class="lc-no">(\d+)</span>', called), ["374", "373", "372", "371"])
        self.assertIn('<time datetime="2026-11-27">27 Nov 2026</time>, 50:26', called)
        self.assertIn("The one with the kicking off and a sleep over at Jenny's", called)
        self.assertIn(SHOW + "6b085a07f82f6a279ca04db5", called)

    def test_outside_markers_unchanged(self):
        strip = re.compile(r"<!-- (episodes:[\w-]+):start -->.*?<!-- \1:end -->", re.S)
        old = strip.sub("", self.before.decode("utf-8"))
        new = strip.sub("", self.page.read_text(encoding="utf-8"))
        self.assertEqual(old, new)

    def test_second_run_changes_nothing(self):
        after = self.page.read_bytes()
        code, _, _ = self.run_script("feed-new-episode.xml")
        self.assertEqual(code, 0)
        self.assertEqual(self.page.read_bytes(), after)


class BadFeedTest(PageTestCase):
    """(c) A bad feed changes nothing and exits non-zero."""

    def assert_refused(self, feed):
        for extra in ([], ["--check"]):
            code, _, err = self.run_script(feed, *extra)
            self.assertEqual(code, 2, err)
            self.assertIn("not changed", err)
            self.assertEqual(self.page.read_bytes(), self.before)
            self.assertEqual(self.sitemap.read_bytes(), self.sitemap_before)

    def test_broken_feed(self):
        self.assert_refused("feed-broken.xml")

    def test_feed_without_episode_numbers(self):
        self.assert_refused("feed-no-numbers.xml")

    def test_feed_with_too_few_episodes(self):
        self.assert_refused("feed-short.xml")

    def test_missing_feed(self):
        self.assert_refused("no-such-feed.xml")

    def test_older_item_without_number_is_skipped(self):
        feed = (FIXTURES / "feed-current.xml").read_text(encoding="utf-8")
        feed = feed.replace("Ep 368. The one with the new double act", "A sick note from HQ")
        episodes = update_episodes.parse_feed(feed.encode("utf-8"))
        numbers = [episode.number for episode in episodes]
        self.assertNotIn(368, numbers)
        self.assertEqual(len(numbers), update_episodes.NEEDED)

    def test_repost_of_an_old_episode_is_skipped(self):
        feed = (FIXTURES / "feed-current.xml").read_text(encoding="utf-8")
        # A repost of episode 200 between 370 and 371 must not stop the update.
        feed = feed.replace("Ep 370.", "Ep 200.", 1)
        episodes = update_episodes.parse_feed(feed.encode("utf-8"))
        numbers = [episode.number for episode in episodes]
        self.assertNotIn(200, numbers)
        self.assertNotIn(370, numbers)
        self.assertEqual(numbers[0], 374)
        self.assertEqual(numbers, sorted(numbers, reverse=True))
        self.assertEqual(len(numbers), update_episodes.NEEDED)

    def test_repost_as_the_newest_item(self):
        feed = (FIXTURES / "feed-new-episode.xml").read_text(encoding="utf-8")
        # The newest item is a repost of episode 373. Episode 374 stays the latest.
        feed = feed.replace("<title>Ep 375.", "<title>Ep 373.", 1)
        episodes = update_episodes.parse_feed(feed.encode("utf-8"))
        self.assertEqual(episodes[0].number, 374)
        self.assertEqual(len({episode.number for episode in episodes}), update_episodes.NEEDED)

    def test_page_without_markers(self):
        self.page.write_text("<p>No markers</p>\n", encoding="utf-8")
        self.before = self.page.read_bytes()
        self.assert_refused("feed-current.xml")


class LivePageTest(unittest.TestCase):
    def test_live_page_has_every_marker_pair(self):
        episodes = update_episodes.parse_feed((FIXTURES / "feed-current.xml").read_bytes())
        page = LIVE_PAGE.read_text(encoding="utf-8")
        update_episodes.apply_sections(page, update_episodes.render_sections(episodes))


class HelperTest(unittest.TestCase):
    def test_title_prefixes(self):
        for raw, number, title in [
            ("Ep 374. The one with polls ", 374, "The one with polls"),
            ("Ep. 366 The one with CostCo", 366, "The one with CostCo"),
            ("Ep 124.The one with a party", 124, "The one with a party"),
            ("Episode 12: The one", 12, "The one"),
        ]:
            item = update_episodes.ET.fromstring("<item/>")
            self.assertEqual(update_episodes.parse_number(item, raw), number, raw)
            self.assertEqual(update_episodes.clean_title(raw), title, raw)

    def test_title_without_number(self):
        item = update_episodes.ET.fromstring("<item/>")
        self.assertIsNone(update_episodes.parse_number(item, "A sick note from HQ"))
        self.assertIsNone(update_episodes.parse_number(item, "2026 in review"))
        self.assertIsNone(update_episodes.parse_number(item, "2027: the tour is on sale"))

    def test_sitemap_lastmod(self):
        sitemap = (HERE.parent / "sitemap.xml").read_text(encoding="utf-8")
        day = update_episodes.datetime.date(2026, 12, 4)
        new = update_episodes.update_sitemap(sitemap, day)
        self.assertIn(
            f"<loc>{update_episodes.HOME_URL}</loc>\n    <lastmod>2026-12-04</lastmod>", new
        )
        # Only the home page changes.
        self.assertEqual(new.count("2026-12-04"), 1)
        with self.assertRaises(update_episodes.FeedError):
            update_episodes.update_sitemap("<urlset/>", day)

    def test_episode_field_wins(self):
        item = update_episodes.ET.fromstring(
            '<item xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">'
            "<itunes:episode>400</itunes:episode></item>"
        )
        self.assertEqual(update_episodes.parse_number(item, "Ep 374. Title"), 400)

    def test_durations(self):
        for raw, shown in [("50:26", "50:26"), ("3026", "50:26"), ("1:02:58", "1:02:58"),
                           ("62:58", "1:02:58"), ("5:03", "5:03"), ("00:59:01", "59:01")]:
            self.assertEqual(update_episodes.format_duration(raw), shown, raw)
        with self.assertRaises(update_episodes.FeedError):
            update_episodes.format_duration("about an hour")

    def test_dates(self):
        day = update_episodes.parse_date("Fri, 27 Nov 2026 02:02:00 GMT")
        self.assertEqual(update_episodes.long_date(day), "27 November 2026")
        self.assertEqual(update_episodes.short_date(day), "27 Nov 2026")
        # 23:30 GMT in summer is the next day in London.
        late = update_episodes.parse_date("Thu, 13 Aug 2026 23:30:00 GMT")
        self.assertEqual(late.isoformat(), "2026-08-14")


if __name__ == "__main__":
    unittest.main()
