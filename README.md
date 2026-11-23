# Monday 23 November 2026: 32 date-checked stories, 6 regions, 13 illustrations

![stories](https://img.shields.io/badge/stories-32-blue)
![regions](https://img.shields.io/badge/regions-6-green)
![license](https://img.shields.io/badge/license-MIT-yellow)

One image that sums up the world's news of Monday 23 November 2026:
32 stories, 6 regions, 13 flat-drawn illustrations, a world map with
numbered pins, a "day in numbers" strip, and a DATE CHECK footer that
names the stories left out because they belong to other days.

Lead story: a Houthi missile is downed over western Saudi Arabia as
the Iran war spreads to the Gulf (Al Jazeera, Reuters). Every story on
the page happened, or was first reported, on 23 November 2026 — the
Trump–Xi–Putin summit (19 Nov), the COP31 collapse (22 Nov), the
Democrats' 258 House seats (22 Nov) and the Starship catch (14 Nov)
are listed in the footer as other days' news, not as today's.

## How it runs

`main.py` is standard library only: it copies the bundled `entry.png`
(a 1024×1024 PNG, 180,892 bytes) to `/output/entry.png`, verifying the
PNG magic bytes, the 1 MiB gate, the SHA-256 and the exact size before
writing, and re-reading the written copy to confirm it matches. No
network, no third-party packages, deterministic — both runs write the
same bytes.

## Competition

Entry for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123)
("Sum up 23 November's world news in one image", $100).
