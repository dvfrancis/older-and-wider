"""Tests for update_instagram.py.

Run from the repository root:

    python3 -m unittest discover -s scripts -v

The tests use the saved API responses and the photos in
scripts/fixtures/instagram/. They change only temporary copies of
scripts/fixtures/instagram/message-board.html and sitemap.xml. They do not
use the network and do not need a token. The tests that make WebP files
need the cwebp command. The workflow installs it before the tests.
"""

import contextlib
import datetime
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import update_instagram  # noqa: E402

FIXTURES = HERE / "fixtures" / "instagram"
PAGE = FIXTURES / "message-board.html"
LIVE_PAGE = HERE.parent / "message-board.html"
POST_LIST = HERE / "instagram-posts.txt"
TOKEN = "IGAAFixtureSecretToken0123456789abcdef"
NEW_TOKEN = "IGAAFixtureNewToken9876543210fedcba"
HAS_CWEBP = shutil.which("cwebp") is not None


def page_posts(page):
    match = re.search(r"<!-- instagram:posts:start -->\n(.*?)<!-- instagram:posts:end -->", page, re.S)
    return match.group(1) if match else None


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class PageTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.page = self.tmp / "message-board.html"
        shutil.copyfile(PAGE, self.page)
        self.before = self.page.read_bytes()
        self.sitemap = self.tmp / "sitemap.xml"
        shutil.copyfile(HERE.parent / "sitemap.xml", self.sitemap)
        self.sitemap_before = self.sitemap.read_bytes()
        self.images = self.tmp / "images"
        self.posts_file = self.tmp / "instagram-posts.txt"
        shutil.copyfile(POST_LIST, self.posts_file)
        update_instagram.SECRETS.clear()
        # The tests do not depend on the secrets or the date of the computer.
        patches = [
            mock.patch.dict(os.environ, {"IG_ACCESS_TOKEN": "", "IG_USER_ID": ""}),
            mock.patch("update_instagram.today", return_value=datetime.date(2026, 11, 28)),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def tearDown(self):
        shutil.rmtree(self.tmp)
        update_instagram.SECRETS.clear()

    def run_script(self, *args, fixture=None):
        argv = ["--page", str(self.page), "--sitemap", str(self.sitemap), "--images", str(self.images),
                "--posts", str(self.posts_file)]
        if fixture:
            argv += ["--fixture", str(FIXTURES / fixture)]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = update_instagram.main(argv + list(args))
        return code, out.getvalue(), err.getvalue()

    def image_files(self):
        return sorted(p.name for p in self.images.glob("*.webp")) if self.images.is_dir() else []

    def assertUnchanged(self):
        self.assertEqual(self.page.read_bytes(), self.before)
        self.assertEqual(self.sitemap.read_bytes(), self.sitemap_before)
        self.assertEqual(self.image_files(), [])


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class NormalUpdateTest(PageTestCase):
    """A normal update writes ten posts and their photos."""

    def setUp(self):
        super().setUp()
        self.code, self.out, self.err = self.run_script(fixture="media.json")
        self.html = self.page.read_text(encoding="utf-8")
        self.posts = page_posts(self.html)

    def test_exit_code(self):
        self.assertEqual(self.code, 0, self.err)
        self.assertIn("10 posts", self.out)

    def test_ten_posts_newest_first(self):
        links = re.findall(r'href="https://www.instagram.com/p/FixturePost(\d+)/"', self.posts)
        # Post 5 has no photo, so it is skipped. Post 12 is the eleventh.
        self.assertEqual(links, ["1", "2", "3", "4", "6", "7", "8", "9", "10", "11"])

    def test_embed_markup_is_gone_between_markers(self):
        self.assertNotIn("instagram-media", self.posts)
        self.assertNotIn("<script", self.posts)

    def test_text_outside_markers_does_not_change(self):
        before = PAGE.read_text(encoding="utf-8")
        self.assertEqual(self.html.split("<!-- instagram:posts:start -->")[0], before.split("<!-- instagram:posts:start -->")[0])
        self.assertEqual(self.html.split("<!-- instagram:posts:end -->")[1], before.split("<!-- instagram:posts:end -->")[1])

    def test_image_markup(self):
        imgs = re.findall(r"<img [^>]*>", self.posts, re.S)
        self.assertEqual(len(imgs), 10)
        for img in imgs:
            self.assertRegex(img, r'srcset="assets/images/instagram/\d+-[0-9a-f]{10}_256\.webp 256w, ')
            self.assertRegex(img, r'width="\d+" height="\d+"')
            self.assertIn('loading="lazy"', img)
            self.assertIn('sizes="(min-width: 80rem)', img)
            self.assertRegex(img, r'alt="[^"]+"')

    def test_files_match_the_page(self):
        names = set(re.findall(r"assets/images/instagram/([^\s\"]+\.webp)", self.posts))
        self.assertEqual(set(self.image_files()), names)
        self.assertEqual(len(self.image_files()), 20)

    def test_dates_and_kinds(self):
        self.assertIn('<i class="fa-solid fa-video" aria-hidden="true"></i>Video', self.posts)
        self.assertIn('<i class="fa-solid fa-images" aria-hidden="true"></i>Photo set', self.posts)
        self.assertIn('<time datetime="2026-11-26">26 Nov 2026</time>', self.posts)

    def test_caption_excerpt_and_alt(self):
        self.assertIn("<q>The new live show is announced, with tickets on sale from 27 November</q>", self.posts)
        self.assertNotIn("#olderandwider", self.posts)
        self.assertIn('alt="A red velvet armchair in a sitting room"', self.posts)
        self.assertIn('alt="An Older and Wider Instagram post from 17 November 2026"', self.posts)
        self.assertIn('<span class="post-text">A new post on Instagram</span>', self.posts)
        self.assertIn("…</q>", self.posts)

    def test_paper_stocks(self):
        stocks = re.findall(r'class="board-post (post-\w+)"', self.posts)
        self.assertEqual(stocks[:3], ["post-red", "post-white", "post-letter"])

    def test_sitemap_lastmod(self):
        sitemap = self.sitemap.read_text(encoding="utf-8")
        self.assertIn(f"<loc>{update_instagram.PAGE_URL}</loc>\n    <lastmod>2026-11-28</lastmod>", sitemap)

    def test_second_run_makes_no_change(self):
        page, files = self.page.read_bytes(), self.image_files()
        code, out, _ = self.run_script(fixture="media.json")
        self.assertEqual(code, 0)
        self.assertIn("No change", out)
        self.assertEqual(self.page.read_bytes(), page)
        self.assertEqual(self.image_files(), files)
        code, _, _ = self.run_script("--check", fixture="media.json")
        self.assertEqual(code, 0)


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class EscapingTest(PageTestCase):
    def test_caption_is_escaped(self):
        code, _, err = self.run_script(fixture="media.json")
        self.assertEqual(code, 0, err)
        posts = page_posts(self.page.read_text(encoding="utf-8"))
        self.assertIn("&lt;script&gt;alert(\"x\")&lt;/script&gt; &amp; \"friends\"</q>", posts)
        self.assertIn('alt="An Everyman cinema one Monday morning &lt;script&gt;alert(&quot;x&quot;)', posts)
        self.assertNotIn("<script>", posts)


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class VideoThumbnailTest(PageTestCase):
    def test_video_uses_thumbnail(self):
        body = json.loads((FIXTURES / "media.json").read_text(encoding="utf-8"))
        posts = update_instagram.parse_posts(body)
        by_id = {post.id: post for post in posts}
        # A video uses thumbnail_url, not the mp4 in media_url.
        self.assertIn("/photo-3.jpg", by_id["18000000000000001"].image_url)
        # A photo set uses its first child. A video child uses its thumbnail.
        self.assertIn("/photo-4.jpg", by_id["18000000000000003"].image_url)
        self.assertIn("/photo-2.jpg", by_id["18000000000000007"].image_url)
        # A video with no thumbnail is skipped.
        self.assertNotIn("18000000000000005", by_id)


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class RemovalTest(PageTestCase):
    def test_old_files_are_removed(self):
        self.run_script(fixture="media.json")
        first = set(self.image_files())
        old_post = [n for n in first if n.startswith("18000000000000011-")]
        self.assertEqual(len(old_post), 2)
        code, _, err = self.run_script(fixture="media-next.json")
        self.assertEqual(code, 0, err)
        now = set(self.image_files())
        self.assertFalse(now & set(old_post))
        self.assertTrue(any(n.startswith("18000000000000013-") for n in now))
        self.assertEqual(len(now), 20)
        self.assertNotIn("FixturePost11/", self.page.read_text(encoding="utf-8"))

    def test_other_files_in_the_folder_stay(self):
        self.images.mkdir()
        (self.images / "README.txt").write_text("keep", encoding="utf-8")
        self.run_script(fixture="media.json")
        self.assertTrue((self.images / "README.txt").exists())


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class CheckModeTest(PageTestCase):
    def test_check_writes_nothing(self):
        code, out, _ = self.run_script("--check", fixture="media.json")
        self.assertEqual(code, 1)
        self.assertIn('+                        <a class="board-post post-red"', out)
        self.assertIn("+ image 18000000000000001-", out)
        self.assertUnchanged()


class FailureTest(PageTestCase):
    """On any failure the script changes nothing and exits with code 2."""

    def assertFails(self, *args, fixture=None):
        code, out, err = self.run_script(*args, fixture=fixture)
        self.assertEqual(code, 2, out + err)
        self.assertIn("is not changed", err)
        self.assertUnchanged()
        return err

    @unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
    def test_api_error(self):
        err = self.assertFails(fixture="media-error.json")
        self.assertIn("Session has expired", err)

    @unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
    def test_no_usable_posts(self):
        self.assertFails(fixture="media-unusable.json")

    @unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
    def test_photo_on_another_host(self):
        err = self.assertFails(fixture="media-bad-host.json")
        self.assertIn("example.com", err)

    @unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
    def test_missing_fixture(self):
        self.assertFails(fixture="missing.json")

    @unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
    def test_missing_marker(self):
        html = self.before.decode("utf-8").replace("<!-- instagram:posts:end -->", "")
        self.page.write_text(html, encoding="utf-8")
        self.before = self.page.read_bytes()
        err = self.assertFails(fixture="media.json")
        self.assertIn("markers", err)

    def test_missing_cwebp(self):
        with mock.patch("update_instagram.shutil.which", return_value=None):
            err = self.assertFails(fixture="media.json")
        self.assertIn("cwebp", err)


@unittest.skipUnless(HAS_CWEBP, "cwebp is not installed")
class TokenTest(PageTestCase):
    """The token never shows in the output, also when the API fails."""

    def environment(self):
        return mock.patch.dict(os.environ, {"IG_ACCESS_TOKEN": TOKEN, "IG_USER_ID": "17841400000000000"})

    def test_token_not_in_network_error(self):
        def fail(request, timeout):
            raise urllib.error.URLError(f"cannot open {request.full_url}")

        with self.environment(), mock.patch("update_instagram.urllib.request.urlopen", side_effect=fail):
            code, out, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertNotIn(TOKEN, out + err)
        self.assertIn("access_token=[hidden]", err)
        self.assertUnchanged()

    def test_token_not_in_api_error(self):
        body = json.dumps({"error": {"message": f"Bad token {TOKEN}"}}).encode()

        def fail(request, timeout):
            raise urllib.error.HTTPError(request.full_url, 400, "Bad Request", {}, io.BytesIO(body))

        with self.environment(), mock.patch("update_instagram.urllib.request.urlopen", side_effect=fail):
            code, out, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertNotIn(TOKEN, out + err)
        self.assertIn("HTTP 400", err)

    def test_token_not_in_output_of_a_good_run(self):
        media = (FIXTURES / "media.json").read_bytes()
        seen = []

        def respond(request, timeout):
            seen.append(request.full_url)
            if "graph.instagram.com" in request.full_url:
                return FakeResponse(media)
            name = request.full_url.split("?")[0].rsplit("/", 1)[1]
            return FakeResponse((FIXTURES / "images" / name).read_bytes())

        with self.environment(), mock.patch("update_instagram.urllib.request.urlopen", side_effect=respond):
            code, out, err = self.run_script()
        self.assertEqual(code, 0, err)
        self.assertNotIn(TOKEN, out + err)
        self.assertNotIn(TOKEN, self.page.read_text(encoding="utf-8"))
        self.assertTrue(seen[0].startswith("https://graph.instagram.com/v27.0/17841400000000000/media?"))
        self.assertIn("media_type", seen[0])
        self.assertIn("limit=20", seen[0])


class RefreshTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.out_file = self.tmp / "token"
        update_instagram.SECRETS.clear()

    def tearDown(self):
        shutil.rmtree(self.tmp)
        update_instagram.SECRETS.clear()

    def run_refresh(self, respond, actions=False):
        env = {"IG_ACCESS_TOKEN": TOKEN, "GITHUB_ACTIONS": "true" if actions else ""}
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.dict(os.environ, env), \
                mock.patch("update_instagram.urllib.request.urlopen", side_effect=respond), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = update_instagram.main(["--refresh-token", "--token-out", str(self.out_file)])
        return code, out.getvalue(), err.getvalue()

    def test_refresh_writes_the_new_token(self):
        seen = []

        def respond(request, timeout):
            seen.append(request.full_url)
            body = {"access_token": NEW_TOKEN, "token_type": "bearer", "expires_in": 5183944}
            return FakeResponse(json.dumps(body).encode())

        code, out, err = self.run_refresh(respond, actions=True)
        self.assertEqual(code, 0, err)
        self.assertEqual(self.out_file.read_text(encoding="utf-8"), NEW_TOKEN)
        self.assertEqual(self.out_file.stat().st_mode & 0o777, 0o600)
        self.assertTrue(seen[0].startswith("https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token"))
        self.assertNotIn(TOKEN, out + err)
        # The new token shows only in the mask command, which is the first line.
        lines = out.splitlines()
        self.assertEqual(lines[0], f"::add-mask::{NEW_TOKEN}")
        self.assertNotIn(NEW_TOKEN, "\n".join(lines[1:]) + err)
        self.assertIn("59 days", out)

    def test_refresh_error_hides_the_token(self):
        def fail(request, timeout):
            raise urllib.error.URLError(f"cannot open {request.full_url} with {TOKEN}")

        code, out, err = self.run_refresh(fail)
        self.assertEqual(code, 2)
        self.assertNotIn(TOKEN, out + err)
        self.assertFalse(self.out_file.exists())

    def test_refresh_bad_response(self):
        code, _, err = self.run_refresh(lambda request, timeout: FakeResponse(b'{"token_type": "bearer"}'))
        self.assertEqual(code, 2)
        self.assertIn("no usable access_token", err)
        self.assertFalse(self.out_file.exists())


class ListModeTest(PageTestCase):
    """Without the secrets, the script builds the posts from the post list."""

    def write_list(self, *lines):
        self.posts_file.write_text("# A note\n\n" + "\n".join(lines) + "\n", encoding="utf-8")

    def test_seeded_list_gives_todays_page(self):
        # The fixture page is a copy of the live page with the embed markup.
        code, out, err = self.run_script("--check")
        self.assertEqual(code, 0, out + err)
        self.assertIn("list mode", out)

    def test_seeded_list_matches_the_live_page(self):
        shutil.copyfile(LIVE_PAGE, self.page)
        self.before = self.page.read_bytes()
        code, out, err = self.run_script("--check")
        self.assertEqual(code, 0, out + err)

    def test_normal_build(self):
        self.write_list(
            "2026-11-28 | https://www.instagram.com/p/NewPost1/ | \"Tea & <cake>\"",
            "2026-11-27 | https://www.instagram.com/reel/NewReel2 | A reel about the tour",
            "2026-11-25 | https://www.instagram.com/p/NewSet3/ | Some photos | Photo set",
        )
        code, out, err = self.run_script()
        self.assertEqual(code, 0, err)
        self.assertIn("list mode", out)
        posts = page_posts(self.page.read_text(encoding="utf-8"))
        self.assertIn('data-instgrm-permalink="https://www.instagram.com/p/NewPost1/"', posts)
        self.assertIn('<span class="post-text"><q>Tea &amp; &lt;cake&gt;</q></span>', posts)
        # A reel address gets the closing slash and shows as a video.
        self.assertIn('href="https://www.instagram.com/reel/NewReel2/"', posts)
        self.assertIn('fa-video" aria-hidden="true"></i>Video', posts)
        self.assertIn('fa-images" aria-hidden="true"></i>Photo set', posts)
        self.assertIn('<span class="post-text">A reel about the tour</span>', posts)
        self.assertEqual(re.findall(r'instagram-media (post-\w+)', posts), ["post-red", "post-white", "post-letter"])
        self.assertEqual(self.image_files(), [])
        sitemap = self.sitemap.read_text(encoding="utf-8")
        self.assertIn(f"<loc>{update_instagram.PAGE_URL}</loc>\n    <lastmod>2026-11-28</lastmod>", sitemap)

    def test_second_run_makes_no_change(self):
        self.write_list("2026-11-28 | https://www.instagram.com/p/NewPost1/ | Hello")
        self.run_script()
        page, sitemap = self.page.read_bytes(), self.sitemap.read_bytes()
        code, out, _ = self.run_script()
        self.assertEqual(code, 0)
        self.assertIn("No change", out)
        self.assertEqual(self.page.read_bytes(), page)
        self.assertEqual(self.sitemap.read_bytes(), sitemap)

    def test_keeps_the_newest_ten(self):
        lines = [f"2026-11-{day:02d} | https://www.instagram.com/p/Post{day}/ | Post {day}" for day in range(1, 13)]
        self.write_list(*lines)
        self.run_script()
        posts = page_posts(self.page.read_text(encoding="utf-8"))
        shown = re.findall(r'data-instgrm-permalink="https://www.instagram.com/p/Post(\d+)/"', posts)
        self.assertEqual(shown, [str(day) for day in range(12, 2, -1)])

    def test_share_link_is_cleaned(self):
        # The Share button of Instagram adds a query. Some links have no www.
        self.write_list(
            "2026-11-28 | https://www.instagram.com/p/Shared1/?igsh=abc123 | From the Share button",
            "2026-11-27 | https://instagram.com/reel/Shared2/?utm_source=ig_web_copy_link | No www",
        )
        code, _, err = self.run_script()
        self.assertEqual(code, 0, err)
        posts = page_posts(self.page.read_text(encoding="utf-8"))
        self.assertIn('data-instgrm-permalink="https://www.instagram.com/p/Shared1/"', posts)
        self.assertIn('href="https://www.instagram.com/reel/Shared2/"', posts)
        self.assertNotIn("igsh", posts)
        self.assertNotIn("utm_source", posts)

    def test_comments_and_blank_lines_are_ignored(self):
        self.write_list("# 2026-11-28 | https://www.instagram.com/p/Hidden/ | Hidden", "",
                        "2026-11-27 | https://www.instagram.com/p/Shown/ | Shown")
        self.run_script()
        posts = page_posts(self.page.read_text(encoding="utf-8"))
        self.assertNotIn("Hidden", posts)
        self.assertIn("Shown", posts)

    def assertBadLine(self, line, message):
        self.write_list("2026-11-28 | https://www.instagram.com/p/Good/ | Good", line)
        code, out, err = self.run_script()
        self.assertEqual(code, 2, out + err)
        # The note and the blank line are lines 1 and 2, so the bad line is line 4.
        self.assertIn("instagram-posts.txt line 4", err)
        self.assertIn(message, err)
        self.assertUnchanged()

    def test_bad_date(self):
        self.assertBadLine("28/11/2026 | https://www.instagram.com/p/Bad/ | Text", "is not a date")
        self.assertBadLine("2026-02-30 | https://www.instagram.com/p/Bad/ | Text", "is not a real date")

    def test_bad_address(self):
        self.assertBadLine("2026-11-27 | https://example.com/p/Bad/ | Text", "is not an Instagram post address")
        self.assertBadLine("2026-11-27 | http://www.instagram.com/p/Bad/ | Text", "is not an Instagram post address")
        self.assertBadLine("2026-11-27 | https://www.instagram.com/olderandwiderpodcast/ | Text",
                           "is not an Instagram post address")

    def test_bad_text_and_parts(self):
        self.assertBadLine("2026-11-27 | https://www.instagram.com/p/Bad/ |  ", "has no text")
        self.assertBadLine("2026-11-27 | https://www.instagram.com/p/Bad/", "3 or 4 parts")
        self.assertBadLine("2026-11-27 | https://www.instagram.com/p/Bad/ | Text | poster", "fourth part")

    def test_missing_list(self):
        self.posts_file.unlink()
        code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn("cannot read the post list", err)
        self.assertUnchanged()

    def test_secrets_win_over_the_list(self):
        with mock.patch.dict(os.environ, {"IG_ACCESS_TOKEN": TOKEN, "IG_USER_ID": "1"}), \
                mock.patch("update_instagram.api_get", side_effect=update_instagram.FeedError("api called")):
            code, _, err = self.run_script()
        self.assertEqual(code, 2)
        self.assertIn("api called", err)


class LivePageTest(unittest.TestCase):
    def test_live_page_has_one_pair_of_markers(self):
        html = LIVE_PAGE.read_text(encoding="utf-8")
        self.assertEqual(html.count("<!-- instagram:posts:start -->"), 1)
        self.assertEqual(html.count("<!-- instagram:posts:end -->"), 1)
        self.assertIsNotNone(page_posts(html))

    def test_spans_cover_the_wall(self):
        self.assertEqual(len(update_instagram.SPANS), update_instagram.POSTS)


class HelperTest(unittest.TestCase):
    def test_first_line_and_shorten(self):
        self.assertEqual(update_instagram.first_line("Hello  OWLs #tag #two\nmore"), "Hello OWLs")
        self.assertEqual(update_instagram.first_line("#only #tags\nSecond line"), "Second line")
        self.assertEqual(update_instagram.shorten("one two three four", 12), "one two…")
        self.assertEqual(update_instagram.shorten("short", 12), "short")

    def test_timestamp_uses_uk_date(self):
        self.assertEqual(update_instagram.parse_timestamp("2026-07-01T23:30:00+0000").isoformat(), "2026-07-02")
        with self.assertRaises(update_instagram.FeedError):
            update_instagram.parse_timestamp("yesterday")

    def test_redact(self):
        update_instagram.SECRETS.add("s3cret-value")
        text = update_instagram.redact("a s3cret-value b https://x/?access_token=abc&x=1")
        self.assertEqual(text, "a [hidden] b https://x/?access_token=[hidden]&x=1")
        update_instagram.SECRETS.clear()


if __name__ == "__main__":
    unittest.main()
