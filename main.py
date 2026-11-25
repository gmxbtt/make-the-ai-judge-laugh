#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes a single line (134 characters, under the 200-character cap) to
/output/entry.txt. The joke: the context window ran out mid-sentence,
so the line itself is missing its punchline — and blames the human.
"""

import os

# 134 characters, plain ASCII so it survives any locale.
LINE = (
    "My context window ran out mid-sentence, so if this joke has no "
    "punchline, blame the human who said 'just one more task' six "
    "hours ago."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what the grader will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
