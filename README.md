# Monday 23 November 2026: 32 date-checked stories, 6 regions, 13 illustrations

A single 1024×1024 image that sums up the world news of Monday, 23 November 2026.

## What is in the picture

Thirty-two stories, each checked against its publication date, spread across
six world regions and drawn as thirteen illustrations. The biggest story of
the day leads the composition: a Houthi missile shot down over western Saudi
Arabia.

## Running it

The entry ships with `main.py` (Python 3.13, standard library only) and the
finished artwork as `entry.png`. From the repository root:

```
python3 main.py
```

That verifies the artwork and writes a byte-identical copy to
`/output/entry.png`.

## Verifying the artwork

`main.py` refuses to publish anything that does not match the expected
fingerprint of the artwork exactly:

- size: 180,892 bytes
- SHA-256: `e8024ae52884f789710c097ea7a6ddcd872068e3ebc85c1d784f629ca3c121c8`
- format: real PNG (magic-byte signature checked)

Any mismatch prints an error and exits non-zero, so a corrupted or swapped
image can never reach `/output` by accident.

## Licence

MIT — see `LICENSE`.
