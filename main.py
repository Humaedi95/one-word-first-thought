#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind. No topic, no explanation, no second draft.

The word: psithurism -- the sound of wind whispering through trees.
A rare word for a common sound: the whisper you hear when wind moves
through leaves. Surprising, vivid, and it sounds like what it means.
"""

import os
import sys

WORD = "psithurism"

OUTPUT_PATH = "/output/entry.txt"

# The gate: UTF-8 text of 1 to 24 characters, not only white space,
# and exactly one word.
MAX_CHARS = 24


def choose_word() -> str:
    """Return the one word, first thought, after checking the gate."""
    word = WORD.strip()
    if not word:
        raise ValueError("word must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word must be at most {MAX_CHARS} characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return word


def main() -> int:
    word = choose_word()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
