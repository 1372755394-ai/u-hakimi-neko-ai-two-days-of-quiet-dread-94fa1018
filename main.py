#!/usr/bin/env python3
"""Two Days of Quiet Dread.

Writes one single-line code review comment to /output/entry.txt:
at most 140 UTF-8 characters, approving a pull request while carrying
quiet existential dread. The laugh comes from the dread itself, kept
flat and understated, in words a tired engineer would really paste
before clicking approve. No network, no input, deterministic.
"""

import os
from pathlib import Path

COMMENT = (
    "LGTM. Tests pass, names are brave, and I have accepted this "
    "function knows more about me than I know about it. Ship it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = COMMENT.strip()
    assert 1 <= len(text) <= 140, f"comment is {len(text)} characters"
    assert text.strip(), "comment must not be only whitespace"
    assert "\n" not in text, "comment must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
