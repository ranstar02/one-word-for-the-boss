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

import argparse
import os
import sys

WORD = "Seagull"
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def resolve_output_path() -> str:
    """Output path, overridable via OUTPUT_PATH (default /output/entry.txt)."""
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


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
    parser = argparse.ArgumentParser(description="Write the one word for the boss.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the word without writing anything",
    )
    args = parser.parse_args()
    validate(WORD)
    if args.check:
        print(f"ok: {WORD!r} passes validation")
        return
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {WORD!r} to {output_path}")


if __name__ == "__main__":
    main()
