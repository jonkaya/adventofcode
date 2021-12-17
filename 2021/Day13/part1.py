from typing import List, Set, Tuple

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

    first_inst = fold_instructions.pop(0)
    folded_dots: Set[Tuple[int, int]] = set()

    fold, fold_at = first_inst
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

    return len(folded_dots)


if __name__ == "__main__":
    print(fold_paper())
