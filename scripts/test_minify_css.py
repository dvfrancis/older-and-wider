"""Tests for scripts/minify_css.py.

Run: python3 -m unittest discover -s scripts -v
"""

import re
import unittest
from pathlib import Path

import minify_css

ROOT = Path(__file__).resolve().parent.parent


class MinifyTests(unittest.TestCase):
    def test_removes_comments_and_space(self):
        css = "/* note */\n.a {\n    color: red;\n    margin: 0 auto;\n}\n"
        self.assertEqual(minify_css.minify(css), ".a{color: red;margin: 0 auto}\n")

    def test_keeps_strings(self):
        css = '.a::after {\n    content: "\\2191  /*x*/ ;" / "";\n}\n'
        self.assertEqual(minify_css.minify(css), '.a::after{content: "\\2191  /*x*/ ;" / ""}\n')

    def test_keeps_url(self):
        css = '.a { background: url("../images/a b.webp") , url(../x.svg); }'
        self.assertEqual(minify_css.minify(css), '.a{background: url("../images/a b.webp"),url(../x.svg)}\n')

    def test_keeps_space_before_colon(self):
        self.assertEqual(minify_css.minify(".nav :hover { x: 1 }"), ".nav :hover{x: 1}\n")

    def test_keeps_space_in_calc_and_media(self):
        css = "@media (min-width: 48rem) and (max-width: 64rem) {\n  .a { width: calc(100% - 2rem); }\n}"
        self.assertEqual(
            minify_css.minify(css),
            "@media (min-width: 48rem) and (max-width: 64rem){.a{width: calc(100% - 2rem)}}\n",
        )

    def test_comment_between_words(self):
        self.assertEqual(minify_css.minify(".a{margin:0/**/auto}"), ".a{margin:0 auto}\n")

    def test_main_css_keeps_every_rule(self):
        """The small file has the same strings, braces and declarations."""
        css = (ROOT / "assets/css/main.css").read_text(encoding="utf-8")
        small = minify_css.minify(css)
        self.assertLess(len(small), len(css))
        self.assertEqual(small.count("{"), small.count("}"))
        no_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        self.assertEqual(no_comments.count("{"), small.count("{"))
        strings = re.compile(r'"(?:[^"\\\n]|\\.)*"')
        self.assertEqual(strings.findall(no_comments), strings.findall(small))
        # The same tokens remain after all white space is removed, except the
        # last semicolon of each block.
        def squash(text):
            return re.sub(r";}", "}", re.sub(r"\s+", "", text))
        self.assertEqual(squash(no_comments), squash(small))


if __name__ == "__main__":
    unittest.main()
