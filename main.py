#!/usr/bin/env python3
"""One Line, One Laugh: The Office Joke Open.

Writes a single original one-line joke about office life to
/output/entry.txt (1-200 UTF-8 characters, no trailing newline).
Deterministic, stdlib only, no network, no input.
"""

import os

JOKE = (
    "Our manager banned the phrase 'quick question' after one lasted "
    "forty minutes and spawned a whole new department."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
