"""Write the entry sentence to /output/entry.txt.

One sentence, at most 200 characters, about the best meal ever had.
Pure Python 3.13 standard library; reads MAKEFUN_OUTPUT_DIR only as
a path (default /output).
"""

import hashlib
import os
import sys

ENTRY = (
    "The best meal I ever had was instant noodles eaten standing in "
    "a hospital corridor at 3 a.m., while a nurse told me my father "
    "would be fine and the salt stung the cut on my lip."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    # Verify what landed on disk: exact bytes, length, and hash.
    with open(path, "rb") as handle:
        written = handle.read()
    assert written == data, "entry.txt bytes differ from ENTRY"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {path}: {len(written)} bytes sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
