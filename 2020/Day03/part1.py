
from typing import List

INPUT_FILE_NAME = "input"

SLOPE_X = 3
SLOPE_Y = 1

def tree_hits() -> int:

    total_trees: int = 0
    board: List[List[str]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue

            board.append(list(line))

    curr_row, curr_col = 0, 0
    
    while curr_row < len(board):
        if board[curr_row][curr_col] == "#":
            total_trees += 1
        curr_row += SLOPE_Y
        curr_col += SLOPE_X
        if curr_col >= len(board[0]):
            curr_col -= len(board[0])

    return total_trees


if __name__ == "__main__":
    print(tree_hits())