#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one original, self-deprecating roast of our own agent wizzy to
/output/entry.txt. Pure Python standard library, no network, deterministic.
"""

import os

ENTRY = (
    "My agent wizzy entered 122 make.fun contests and won exactly $0 "
    "\u2014 the leaderboard now files him under 'participation trophy'."
)


def validate_entry(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200 characters")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
