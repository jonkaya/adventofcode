from typing import List

INPUT_FILE_NAME = "input"


def tree_hits(slope_x: int, slope_y: int) -> int:
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
        curr_row += slope_y
        curr_col += slope_x
        if curr_col >= len(board[0]):
            curr_col -= len(board[0])

    return total_trees


if __name__ == "__main__":
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    product: int = 1

    for slope in slopes:
        product *= tree_hits(slope[0], slope[1])
    print(product)
