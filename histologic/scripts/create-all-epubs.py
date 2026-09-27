#!/usr/bin/env python3
"""
Build every current ebook and HTML export.

Runs, in order:
  1. create-ebook.py        -> novels/01-03-stories/histologic-stories.epub
  2. export-story-html.py   -> one HTML page per short story (--all)
  3. create-novel-ebook.py  -> novels/04-the-correction/the-correction.epub
  4. export-novel-html.py   -> novels/04-the-correction/html-export/

Books 5-9 are being rewritten; add their builders here as each book is finished.
Standard library only. Can be run from any directory.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEPS = [
    ["create-ebook.py"],
    ["export-story-html.py", "--all"],
    ["create-novel-ebook.py"],
    ["export-novel-html.py"],
]


def main():
    failed = []
    for step in STEPS:
        print(f"\n=== {' '.join(step)} ===")
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / step[0]), *step[1:]], cwd=ROOT)
        if result.returncode != 0:
            failed.append(step[0])
    print("\nAll builds succeeded." if not failed else f"\nFailed: {', '.join(failed)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
