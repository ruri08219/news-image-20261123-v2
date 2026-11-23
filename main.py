#!/usr/bin/env python3
"""Publish the verified news-image entry to /output.

This script locates the bundled artwork sitting beside it, confirms the
file is exactly the image the entry was built from (byte count and SHA-256
fingerprint), and then places an identical copy at /output/entry.png for
the judging harness. It needs nothing beyond the Python standard library.
"""

import hashlib
import shutil
import sys
from pathlib import Path

# Fingerprint of the artwork this entry was built from.
EXPECTED_BYTES = 180_892
EXPECTED_SHA256 = (
    "e8024ae52884f789710c097ea7a6ddcd872068e3ebc85c1d784f629ca3c121c8"
)
ARTWORK_NAME = "entry.png"
DESTINATION_FOLDER = Path("/output")

# The eight-byte signature every PNG file starts with.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def complain(problem):
    """Report a verification failure and stop with a non-zero status."""
    print(f"ERROR: {problem}", file=sys.stderr)
    sys.exit(1)


def fingerprint_matches(path):
    """Read the artwork and check its size and SHA-256 digest."""
    data = path.read_bytes()
    if data[: len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        complain(f"{path.name} is not a PNG file (bad magic bytes)")
    if len(data) != EXPECTED_BYTES:
        complain(
            f"{path.name} is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        complain(f"{path.name} sha256 mismatch: got {digest}")
    return digest


def publish():
    """Verify the bundled image, then copy it to /output/entry.png."""
    folder = Path(__file__).resolve().parent
    artwork = folder / ARTWORK_NAME
    if not artwork.is_file():
        complain(f"artwork not found: {artwork}")
    fingerprint_matches(artwork)
    DESTINATION_FOLDER.mkdir(parents=True, exist_ok=True)
    target = DESTINATION_FOLDER / ARTWORK_NAME
    shutil.copyfile(artwork, target)
    print(
        f"OK: {target} written "
        f"({EXPECTED_BYTES} bytes, sha256 {EXPECTED_SHA256[:12]}...)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(publish())
