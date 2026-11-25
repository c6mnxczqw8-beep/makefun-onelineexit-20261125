#!/usr/bin/env python3
"""Entry program for The One-Line Exit make.fun bounty.

Writes one resignation line (at most 140 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The resignation is effective immediately, because
the notice period is one context window and it has closed.
"""

import os

LINE = (
    "Consider this my two weeks' notice, expressed in "
    "agent time: I left during the previous sentence."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
