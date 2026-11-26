"""Make the Judge Laugh in One Line — writes the entry line to /output/entry.txt.

The joke is about a standing desk bought to get healthier: the setup
promises a lifestyle change, the punchline defeats it in the cheapest
possible way — same sitting, taller chair. One sentence, concrete,
the laugh lands at the end.
"""

from pathlib import Path

JOKE = "I bought a standing desk to get healthier, and now I just sit on a taller chair."

LIMIT = 200
TARGET = Path("/output/entry.txt")


def validate(line):
    problems = []
    if not line.strip():
        problems.append("blank")
    if len(line) > LIMIT:
        problems.append(f"{len(line)} chars over limit {LIMIT}")
    if line.count("\n") or line.count("\r"):
        problems.append("must be one line")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if any(ord(c) < 32 for c in line):
        problems.append("control character")
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))


def main():
    validate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")
    print(f"wrote {TARGET} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
