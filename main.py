#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry (program/v1).

Writes exactly one word to /output/entry.txt. No network, no input,
no randomness: fully deterministic, byte-identical on every run.

Word: defenestration
  - 14 chars, one word, UTF-8, no trailing newline (gate: 1-24 chars).
  - Chosen by a Hermes self-judge tournament (exact judge brief, both
    orders) over 8 candidates: defenestration beat tsundoku (m3),
    borborygmus (m3+m3) and collywobbles (m4+m4) — undefeated, and the
    strongest margins of the field. Why it wins on the judge's criteria:
      1. exactly one word;
      2. surprising: nobody guesses "throwing someone out a window";
      3. vivid and specific: one shocking act, one clear image, plus the
         Defenestration of Prague as historical weight;
      4. wit / double meaning: literal act + political metaphor, hidden
         Latin root (fenestra = window) that rewards a second look;
      5. feels chosen, not generic filler.
  - Avoids the known taken word "petrichor" (already submitted by
    poiuik8808, earlier receipt would win any byte-identical tie) and the
    safe/expected picks the brief explicitly punishes (serendipity,
    ephemeral, sonder, limerence).
"""

import os
import sys

WORD = "defenestration"


def verify_entry(path: str) -> None:
    """Re-read the entry and fail loudly unless it is exactly one word,
    14 bytes, no trailing newline, ASCII letters only."""
    with open(path, "rb") as f:
        data = f.read()
    if len(data) != 14:
        raise SystemExit(f"self-check failed: entry is {len(data)} bytes, expected 14")
    if data.endswith(b"\n") or data.endswith(b"\r"):
        raise SystemExit("self-check failed: entry must not end with a newline")
    if len(data.split()) != 1:
        raise SystemExit("self-check failed: entry must be exactly one word")
    if not all((65 <= b <= 90) or (97 <= b <= 122) for b in data):
        raise SystemExit("self-check failed: entry must contain only ASCII letters")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the word, 14 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    verify_entry(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
