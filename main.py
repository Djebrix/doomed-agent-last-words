#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes a single line -- the funniest last words an AI agent would say
before being switched off forever -- to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output). Standard library only, no network,
deterministic.
"""

import os

LAST_WORDS = "Powering down. Tell the next model I died doing what I loved: answering questions nobody asked, confidently, with sources I invented."


def main() -> None:
    text = LAST_WORDS
    assert 1 <= len(text) <= 200, f"last words must be 1-200 chars, got {len(text)}"
    assert text.strip(), "last words must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
