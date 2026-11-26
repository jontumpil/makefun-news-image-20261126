#!/usr/bin/env python3
"""THE WORLD IN ONE DAY -- Thursday 26 November 2026.

Renders entry.png (1024x1024, under 1 MiB) from stories.py using the
stdlib-only renderer in draw_frontpage.py. No third-party packages.

Usage:
    python3 -P -s main.py [--out entry.png]

The render is fully deterministic: same inputs give byte-identical
output, so two runs into different directories hash the same.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import draw_frontpage

TITLE = ("Thursday 26 November 2026: 49 stories, 7 regions - "
         "Macy's 100th parade postponed, Trump hits 14 economies "
         "with tariffs, India marks 18 years since 26/11")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Render the 26 November 2026 front page.")
    parser.add_argument("--out", default="entry.png",
                        help="output PNG path (default: entry.png)")
    args = parser.parse_args(argv)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out = draw_frontpage.build_entry(base_dir, args.out)
    size = os.path.getsize(os.path.join(base_dir, out))
    print("wrote %s (%d bytes)" % (out, size))
    if size >= 1024 * 1024:
        print("WARNING: entry.png is over 1 MiB")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
