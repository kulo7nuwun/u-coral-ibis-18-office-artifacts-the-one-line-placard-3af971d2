#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard -- one line, at most 180 characters -- for
an ordinary office object treated as an ancient artifact, to /output/entry.txt.

The placard is a fixed text, so the program is deterministic: every run
writes byte-identical output.
"""

import os

# The placard, built from its catalogue parts so each label element is
# visible in the code: identification, material and date, the inscription,
# the dry verdict, and the provenance. Joined into one line.
PLACARD_PARTS = [
    "Votive tablet (sticky note), paper and weak adhesive, c. 2019.",
    "Inscribed 'call Dave back' in a fading hand;",
    "the god it addressed never answered.",
    "Recovered beneath a keyboard.",
]

PLACARD = " ".join(PLACARD_PARTS)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PLACARD.strip()
    assert 1 <= len(text) <= 180, f"placard is {len(text)} chars, must be 1-180"
    assert "\n" not in text, "placard must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
