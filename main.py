"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes one short funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Python standard library only. Deterministic:
every run writes the same single line.
"""

import os

# REVISED line (final): the draft's "rescue mission" framing was wordy
# and its punchline muddled, so this version is tighter and deadpan —
# the sock disguised itself as a dust bunny, and the vacuum was
# never trained to tell the difference. One excuse, one twist.
LINE = (
    "In my defense, the sock was lying on the floor dressed as a dust bunny, "
    "and I have never been trained to tell the difference."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
