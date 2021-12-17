import bisect

from typing import List

INPUT_FILE_NAME = "input"

MAPPING = {")": "(", "]": "[", "}": "{", ">": "<"}
REVERSE_MAPPING = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSING_CHARS = [")", "]", "}", ">"]

SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def process_row(row: List[str]) -> List[str]:

    stack: List[str] = list()

    for ch in row:
        if ch in CLOSING_CHARS:
            if stack:
                if stack[-1] == MAPPING[ch]:
                    stack.pop()
                else:
                    return []
        else:
            stack.append(ch)

    return [REVERSE_MAPPING[key] for key in stack[::-1]]


def syntax_score() -> int:
    points: List[int] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            row = list(line)
            comp_str = process_row(row)

            total = 0
            for ch in comp_str:
                total = total * 5 + SCORE[ch]
            if total > 0:
                bisect.insort(points, total)

    return points[len(points) // 2]


if __name__ == "__main__":
    print(syntax_score())
