"""Copy the bundled front-page image to /output/entry.png.

Stdlib only: the sandbox installs nothing, so this program uses just
hashlib, os and pathlib. It verifies the bundled PNG's SHA-256 and size
before writing, then re-reads the written copy to confirm it matches.
"""

import hashlib
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
EXPECTED_SHA256 = "e8024ae52884f789710c097ea7a6ddcd872068e3ebc85c1d784f629ca3c121c8"
EXPECTED_BYTES = 180892


def main():
    data = SRC.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG (bad magic bytes)")
    if len(data) > 1048576:
        raise SystemExit("entry.png is over the 1 MiB gate limit")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.png sha256 mismatch")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit("entry.png size mismatch")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    if out.read_bytes() != data:
        raise SystemExit("written copy differs from bundled image")
    print(f"wrote {out} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
