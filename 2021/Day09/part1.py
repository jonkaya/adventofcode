import math

from typing import List

INPUT_FILE_NAME = "input"

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def process_row(rows: List[List[int]]) -> List[int]:
    # process mid row
    assert len(rows) == 3

    result: List[int] = list()

    def get_value_at_index(x: int, y: int) -> int:
        if 0 <= x < len(rows) and 0 <= y < len(rows[0]):
            return rows[x][y]
        else:
            return math.inf

    for i, val in enumerate(rows[1]):
        is_min = True
        for dir in DIRECTIONS:
            newx, newy = 1 + dir[0], i + dir[1]
            if val >= get_value_at_index(newx, newy):
                is_min = False
                break
        if is_min:
            result.append(val)

    return result


def low_points() -> int:
    total_risk_level: int = 0
    window: List[List[int]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            row = list(map(int, list(line)))
            if len(window) == 0:
                window.append([math.inf for _ in range(len(row))])
            window.append(row)

            if len(window) == 3:
                low_pts = process_row(window)
                total_risk_level += sum(low_pts) + len(low_pts)
                window.pop(0)

    # process the final row
    window.append([math.inf for _ in range(len(row))])
    low_pts = process_row(window)
    total_risk_level += sum(low_pts) + len(low_pts)

    return total_risk_level


if __name__ == "__main__":
    print(low_points())
