#!/usr/bin/env python3
"""news-image-20261120 entry: write the broadsheet image to /output/entry.png.

The image (a 1024x1024 PNG summing up Friday 20 November 2026's world news)
is held in this repository as entry.png. This program only copies those exact
bytes to /output/entry.png. Standard library only, no network, deterministic:
two runs write identical bytes.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
EXPECTED_SHA256 = "78e479671808bcacf8259bba94a30a0a5a756f18732d10ce1c26e301a2e9b7e8"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry.png hash mismatch: {digest}", file=sys.stderr)
        return 1
    if len(data) > 1024 * 1024:
        print(f"entry.png too large: {len(data)} bytes", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    print(f"wrote {DST} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
