#!/usr/bin/env python3
"""Make a CSS file smaller for the deploy copy.

build.sh runs this script on each file in deploy/assets/css/. The source file
in assets/css/ does not change.

The script does only safe changes:

- It removes comments.
- It changes each run of white space to one space.
- It removes the spaces next to { } ; and ,
- It removes the last ; before each }.

It does not change the text in strings or in url(). It does not remove a
space next to a colon, because "a :hover" and "a:hover" are different
selectors.

Usage: python3 scripts/minify_css.py FILE [FILE ...]
"""

import re
import sys

# One token: a string, a url(), a comment, white space, or one other character.
TOKEN = re.compile(
    r'"(?:[^"\\\n]|\\.)*"'
    r"|'(?:[^'\\\n]|\\.)*'"
    r"|url\(\s*[^)\"'\s]*\s*\)"
    r"|/\*.*?\*/"
    r"|\s+"
    r"|.",
    re.S,
)

TIGHT = set("{};,")


def minify(css: str) -> str:
    """Return the CSS text with comments and extra white space removed."""
    out: list[str] = []
    for match in TOKEN.finditer(css):
        token = match.group(0)
        if token.startswith("/*"):
            # A comment between two words must not join them.
            token = " "
        if token.isspace():
            if out and (out[-1] == " " or out[-1] in TIGHT):
                continue
            out.append(" ")
            continue
        if token in TIGHT and out and out[-1] == " ":
            out.pop()
        if token == "}" and out and out[-1] == ";":
            out.pop()
        out.append(token)
    return "".join(out).strip() + "\n"


def main(paths: list[str]) -> int:
    if not paths:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            css = handle.read()
        small = minify(css)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(small)
        print(f"{path}: {len(css.encode())} to {len(small.encode())} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
