"""Unsent: The Micro-Confession Sprint.

Writes a two-part micro-confession to entry.txt: a To: line naming who
the message was meant for, and the unsent line itself, exactly as typed.
Stdlib only. Output goes to MAKEFUN_OUTPUT_DIR when set, else the
script directory (grader runs read-only, so honour the env var).
"""

import os

ENTRY = (
    "To: Dad\n"
    "I kept the voicemail where you said you were proud of me, "
    "and I never told you I heard it the day you died.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
