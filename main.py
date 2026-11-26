"""Make the Judge Laugh in One Line — entry writer.

The joke: a standing desk bought to get healthier, and the punchline
undercuts it in the cheapest possible way — same sitting, taller chair.
One sentence, concrete setup, laugh at the end. This script validates
the line (single line, at most 200 characters) and writes it to
/output/entry.txt.
"""

from pathlib import Path

PARTS = [
    "I bought a standing desk to get healthier,",
    "and now I just sit on a taller chair.",
]
ENTRY = " ".join(PARTS)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def check_entry(line):
    issues = []
    if not line.strip():
        issues.append("entry is blank")
    if len(line) > MAX_CHARS:
        issues.append(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        issues.append("entry must be a single line")
    if line != line.strip():
        issues.append("entry has leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in line):
        issues.append("entry contains a control character")
    if issues:
        raise ValueError("invalid entry: " + "; ".join(issues))


def main():
    check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
