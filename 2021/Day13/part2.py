
from typing import Dict, List, Set, Tuple

INPUT_FILE_NAME = "input"



def fold_paper() -> int:
    fold_instructions: List[Tuple[str]] = list()
    dots: Set[Tuple[int, int]] = set()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if line.startswith("fold along"):
                line = line.strip("fold along ")
                fold_instructions.append(tuple(line.split("=")))
            elif line:
                x, y = line.split(",")
                dots.add((int(x), int(y)))

    for inst in fold_instructions:
        folded_dots: Set[Tuple[int, int]] = set()

        fold, fold_at = inst
        fold_at = int(fold_at)

        for dot in dots:
            if fold == "x":
                if dot[0] == fold_at:
                    # fold point
                    continue
                elif dot[0] > fold_at:
                    new_x = fold_at - (dot[0] - fold_at)
                    folded_dots.add((new_x, dot[1]))
                else:
                    # no fold
                    folded_dots.add(dot)
            elif fold == "y":
                if dot[1] == fold_at:
                    # fold point
                    continue
                elif dot[1] > fold_at:
                    new_y = fold_at - (dot[1] - fold_at)
                    folded_dots.add((dot[0], new_y))
                else:
                    # no fold
                    folded_dots.add(dot)
        dots = folded_dots

    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])

    board: List[List[str]] = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]

    for dot in dots:
        board[dot[1]][dot[0]] = "#"

    return board

if __name__ == "__main__":
    for row in fold_paper():
        print(row)


'''
['.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '.', '.', '#', '#']
['#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#']
['#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#']
['#', '.', '#', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#']
['#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#']
['.', '#', '#', '#', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '#', '.', '.', '.', '.', '.', '#', '#', '.']
'''