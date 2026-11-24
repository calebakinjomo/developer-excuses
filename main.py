"""Developer Excuses — one funny single-line excuse for when code breaks in production.

Prints the excuse to stdout and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only.
"""

import os

ENTRY = "I didn't break production — my code just met its first real user and froze, exactly like me in standup."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
