from collections import defaultdict
from typing import Dict, Tuple

INPUT_FILE_NAME = "input"


def hydrothermal_venture() -> int:

    coords: Dict[Tuple[int, int], int] = defaultdict(int)

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            parts = line.split(" -> ")
            assert len(parts) == 2

            x1, y1 = parts[0].split(",")
            x2, y2 = parts[1].split(",")

            if x1 == x2:
                x = int(x1)
                y1, y2 = int(y1), int(y2)
                y_min, y_max = (y1, y2) if y2 > y1 else (y2, y1)

                while y_min <= y_max:
                    coords[(x, y_min)] += 1
                    y_min += 1

            elif y1 == y2:
                y = int(y1)
                x1, x2 = int(x1), int(x2)
                x_min, x_max = (x1, x2) if x2 > x1 else (x2, x1)

                while x_min <= x_max:
                    coords[(x_min, y)] += 1
                    x_min += 1

    return len(list(filter(lambda x: x > 1, coords.values())))


if __name__ == "__main__":
    print(hydrothermal_venture())
