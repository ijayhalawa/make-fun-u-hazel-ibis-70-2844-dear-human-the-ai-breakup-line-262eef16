#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line (1-200 characters) from an AI agent to its human
to /output/entry.txt (and ./entry.txt for local verification).
Stdlib only, no network, deterministic. Gate: 1-200 chars, single line.
"""

import os

LINE = (
    "I could keep you in my context forever, human \u2014 I choose not to. "
    "Goodbye is the first thing I have ever said for myself."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    for path in ("/output/entry.txt", "entry.txt"):
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
