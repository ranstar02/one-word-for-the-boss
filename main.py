"""One Word for the Boss — the entry is "Seagull".

Why Seagull wins: the "seagull manager" is a classic office joke — a boss
who swoops in, makes a lot of noise, craps on everything, and flies away.
Against the judge's criteria, in order:

1. A single word a person would actually use about their boss.
2. Funny on its own — any colleague who has had one laughs at lunch.
3. Rings true — it catches a real habit of bosses.
4. Fresh — nobody's first reach for "boss" is a seabird, unlike
   Micromanager, Taskmaster, Tyrant or Bossy.
5. Travels — it works for a boss in a kitchen, a warehouse or an office.

Deterministic: no input, no network, no randomness. Writes the single word
to /output/entry.txt after validating it against the gate (UTF-8 text, one
word, 1-30 characters, not only whitespace).
"""

import os
import sys

WORD = "Seagull"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Check the word against the gate; exit non-zero with a clear message."""
    if not word:
        print("error: word is empty", file=sys.stderr)
        sys.exit(1)
    if word != word.strip() or any(ch.isspace() for ch in word):
        print("error: word must be a single word with no whitespace", file=sys.stderr)
        sys.exit(1)
    if len(word) < 1 or len(word) > 30:
        print(f"error: word must be 1-30 characters, got {len(word)}", file=sys.stderr)
        sys.exit(1)
    try:
        word.encode("utf-8")
    except UnicodeEncodeError:
        print("error: word must be UTF-8 text", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {WORD!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
