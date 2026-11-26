#!/usr/bin/env python3
"""Rename the Planet.

Writes one funny new name for a planet of our solar system, plus the
why, in a single line under 200 characters, to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 200

LINE = "Venus is now 'The Pressure Cooker': 465 degrees, 92 atmospheres, and it still answers to 'morning star'."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-200 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
