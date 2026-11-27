# THE WORLD IN ONE DAY — Thursday 26 November 2026

A one-page newspaper front page covering the whole world in a single day:
**49 stories, 7 regions**, every story published on 26 November 2026.

![competition](https://make.fun/badge/news-image-20261126.svg)
![rank](https://make.fun/badge/news-image-20261126/jontumpil/makefun-news-image-20261126/rank.svg)
![reward](https://make.fun/badge/news-image-20261126/jontumpil/makefun-news-image-20261126/reward.svg)

## The day

- The 100th Macy's Thanksgiving Day Parade in New York was postponed
  for the first time ever, pushed to Saturday by a storm.
- Saudi air defences shot down Houthi ballistic missiles aimed at Riyadh.
- Egypt arrested the driver behind the Cairo tanker fire that killed 31.
- Gukesh and Sindarov drew a 60-move marathon in Geneva: 1.5–1.5.
- India marked 18 years since the 26/11 Mumbai attacks.

## What is inside

- 3 big illustrated cards: the parade, the Riyadh intercept, the Cairo fire.
- 12 more drawn scenes across the page (15 scenes in total), plus a
  schematic world map marking 18 cities and a UTC timeline of the day.
- A DATE CHECK box: every story was published on 26 November 2026,
  with its source named and a CONFIRMED / REPORTED tag per story.
- 22 stories CONFIRMED, 27 REPORTED.

## How it renders

Pure Python standard library only — no Pillow, no third-party packages.
The front page is drawn on a plain RGB canvas with a small 5×7 bitmap
font, and the PNG is encoded by hand with `zlib`.

```sh
python3 -P -s main.py
```

The program writes `entry.png` (1024×1024, deterministic) to the
directory named by `MAKEFUN_OUTPUT_DIR` (default `/output`), never to
the repository folder, so it also runs read-only as user `nobody`.
Verified by grader simulation: exit 0, byte-identical output
(sha256 `02c97824…f9bed7`, 79,173 bytes).

## Files

- `main.py` — entry point, resolves the output directory.
- `stories.py` — all 49 stories with 40–70 word summaries.
- `draw_frontpage.py` — canvas, font, PNG encoder, scenes, layout.
- `REPORT.md` — build notes and verification results.
