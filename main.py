#!/usr/bin/env python3
"""Rename the Planet — make.fun entry.

Writes one funny new name for a planet, plus the why, in a single line
to /output/entry.txt (created if needed). Standard library only.
"""

import os

LINE = "Jupiter is now 'All-You-Can-Eat' \u2014 it swallowed the other planets' lunches for 4.5 billion years and never apologised."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
