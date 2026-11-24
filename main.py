#!/usr/bin/env python3
"""One Letter for Your Day — entry D.

The letter: D, for "doomscrolling".
My day in one word: I picked up my phone at 9am to check the
weather, looked up again at 9pm, and could not name a single
thing I had actually done in between — only the feed, still
scrolling. D is the most honest letter for a day like that:
a whole day summarized by a thumb that never stopped moving.
"""

import os

LETTER = "D"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isascii() or not LETTER.isalpha():
        raise ValueError("entry must be exactly one A-Z letter")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character, no newline: the gate requires
    # /output/entry.txt to be UTF-8 text of 1 to 1 characters.
    # A trailing newline would make it 2 characters and fail.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(f"Wrote {LETTER!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
