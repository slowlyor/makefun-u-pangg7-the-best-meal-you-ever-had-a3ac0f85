#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt.

Stdlib only, deterministic: the same sentence is written on every run.
"""

import os

SENTENCE = (
    "At a warung in Yogyakarta past midnight, my grandmother pressed a bowl "
    "of soto ayam into my hands, and the first spoonful tasted of turmeric, "
    "lime leaf, and rain falling on the tin roof above us."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
