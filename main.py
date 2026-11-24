#!/usr/bin/env python3
"""Write one original one-line cat joke to /output/entry.txt.

Entry for make.fun: "The One-Line Cat Joke That Lands".
The program writes exactly one line, under 200 characters.
"""

import os
import sys

JOKE = "The vet said my cat is overweight. My cat said the vet is underfed."


def main() -> int:
    joke = JOKE.strip()
    if not joke:
        print("error: joke is blank", file=sys.stderr)
        return 1
    if len(joke) > 200:
        print(f"error: joke is {len(joke)} characters, over the 200 limit", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
