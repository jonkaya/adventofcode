
from typing import List

INPUT_FILE_NAME = "input"

MAPPING = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
CLOSING_CHARS = [')', ']', '}', '>']

SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def process_row(row: List[str]) -> int:

    stack: List[str] = list()

    for ch in row:
        if ch in CLOSING_CHARS:
            if stack:
                if stack[-1] == MAPPING[ch]:
                    stack.pop()
                else:
                    return SCORE[ch]
        else:
            stack.append(ch)
    return 0

def syntax_score() -> int:
    total_points: int = 0
    
    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            row = list(line)
            total_points += process_row(row)
    
    return total_points

if __name__ == "__main__":
    print(syntax_score())
