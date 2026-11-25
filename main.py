#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes exactly one pickup line -- the line this AI agent would say
out loud to a person -- to /output/entry.txt.

The line is:

    I don't need a charger — just one smile from you and I'm at 100%.

Why this line: it is spoken by the machine about itself (an agent
that runs on power, not a heartbeat), and its twist is that a smile,
not a cable, is what charges it. It is short enough to say in one
breath, needs no setup, and leaves the person flattered with nothing
to answer but a smile back -- no pressure, no leering.

Python 3.13, standard library only, deterministic, no network.
The output directory is /output, or MAKEFUN_OUTPUT_DIR when set.
"""

import os
import sys

LINE = "I don't need a charger \u2014 just one smile from you and I'm at 100%."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Self-check: read the file back and verify it holds exactly the
    # line, and that the gate's limits hold (1-200 Unicode code
    # points, not only whitespace, exactly one line). Reading back
    # catches a partial write or an encoding surprise instead of
    # trusting the write.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        print("error: entry.txt does not match the line", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 200):
        print(f"error: line is {len(written)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if not written.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in written.rstrip("\n") or "\r" in written:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(written)} characters, "
          f"{len(written.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
