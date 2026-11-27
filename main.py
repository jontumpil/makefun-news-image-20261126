# main.py -- render THE WORLD IN ONE DAY, 26 November 2026.
# Stdlib only. Writes entry.png to MAKEFUN_OUTPUT_DIR, never to the repo.
# Usage: python3 -P -s main.py [--out entry.png]

import argparse
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import stories
import draw_frontpage


def resolve_output_path(out_arg):
    """Relative --out resolves inside MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if os.path.isabs(out_arg):
        return out_arg
    return os.path.join(out_dir, out_arg)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="entry.png")
    args = parser.parse_args(argv)
    out_path = resolve_output_path(args.out)
    png, stats = draw_frontpage.render_frontpage(stories)
    with open(out_path, "wb") as fh:
        fh.write(png)
    assert os.path.isfile(out_path), out_path
    assert os.path.getsize(out_path) == len(png), out_path
    digest = hashlib.sha256(png).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (out_path, len(png), digest))
    print("stories=%d confirmed=%d reported=%d scenes=%d big_cards=%d"
          % (stories.STORY_COUNT, stats["confirmed"], stats["reported"],
             stats["scenes"], stats["big_cards"]))
    print("column heights: %s" % (stats["columns"],))
    assert len(png) < 1024 * 1024, len(png)
    assert max(stats["columns"]) <= draw_frontpage.GRID_H
    return 0


if __name__ == "__main__":
    sys.exit(main())
