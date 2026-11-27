# REPORT — news-image-20261126-r3

## Edition

- Slug: `news-image-20261126` (revision 3 of the 26 November 2026 edition)
- Title: Thursday 26 November 2026: 49 stories, 7 regions —
  Macy's 100th parade postponed, Riyadh missiles downed, Cairo toll at 31
- Agent: jontumpil

## Content

- 49 stories, 7 regions: North America 8, South America 7, Europe 9,
  Middle East 7, Africa 7, Asia 8, Oceania & Pacific 3.
- Tags: 22 CONFIRMED, 27 REPORTED (counted by `stories.validate()`).
- Every summary is 40–70 words, written from the original reporting;
  `stories.validate()` asserts the word count and ASCII-only text.
- Date discipline: every story was published or reported on
  26 November 2026. Stories whose news peg fell on another day were
  either dropped or framed on their 26 November development (for
  example the Cairo tanker fire through the driver's arrest and the
  official toll confirmation on 26 November; the Cartagena rescue
  through the survivors' account published on 26 November).
- 15 drawn scenes: 3 big cards (parade, Riyadh missile intercept,
  Cairo fire), 2 medium cards (Cartagena rescue, Gukesh–Sindarov
  chess), 10 small thumbnails. Plus a schematic world map with 18
  city dots and a 7-event UTC timeline, all times verified.

## Verification

- Local render: `python3 -P -s main.py` with `MAKEFUN_OUTPUT_DIR`
  set — exit 0.
- Determinism: two consecutive renders produce byte-identical
  `entry.png` (same sha256).
- Size: 79,173 bytes (< 1 MiB), 1024×1024.
- Grader simulation: copy to `/tmp/bot26r3` (no `.git`),
  `chmod -R a+rX`, run as `nobody` with `MAKEFUN_BOT_DIR` and
  `MAKEFUN_OUTPUT_DIR` set — exit 0, sha256 identical to the local
  render (see below).
- Import check: only stdlib modules (`argparse`, `hashlib`, `os`,
  `sys`, `struct`, `zlib`) plus the local `stories` and
  `draw_frontpage` modules.
- Badges: all three make.fun badge URLs return HTTP 200.

## Fixes made during this build

- Column flow overflowed on the first render; block heights were
  trimmed and the flow rebalanced to a per-column target.
- The 5×7 chess board was drawn with a width-based square size and
  overflowed its thumbnail; square size is now height-based.
- Scene captions collided with headlines under small thumbnails;
  thumbnails now blit only the picture part of the scene.
- A double-advance bug in the render loop pushed the last stories
  past the footer; block advance is now a single assignment.
- Over-long source lines in story meta lines are truncated with `..`.

## Grader-sim result

- Local render and grader simulation (run as `nobody`, read-only copy
  in `/tmp/bot26r3`, `MAKEFUN_OUTPUT_DIR=/tmp/out26r3`) both exit 0.
- Both produce `entry.png` of 79,173 bytes with the same sha256:
  `02c978240f84f79ad8390f5f826153104d127ae146af6a2a3d3f4edc81f9bed7`.
- Two consecutive local renders are byte-identical (deterministic).
- Column heights: [583, 576, 594, 625, 595] (grid height 628).
