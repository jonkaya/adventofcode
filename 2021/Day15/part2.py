import heapq

from typing import Dict, List, Tuple

INPUT_FILE_NAME = "input"

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def build_5x_grid(grid: List[List[int]]) -> List[List[int]]:
    result = [[cell for cell in row] for row in grid]
    rows = len(grid)

    for i in range(len(result)):
        for j in range(1, 5):
            new_row = [cell + j if cell + j < 10 else cell + j - 9 for cell in grid[i]]
            result[i].extend(new_row)

    row = 0
    while len(result) < 5 * rows:
        j = len(result) // rows
        new_row = [cell + j if cell + j < 10 else cell + j - 9 for cell in result[row]]
        result.append(new_row)
        row += 1
        row %= rows

    return result


def lowest_risk_path() -> int:
    grid: List[List[int]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue
            grid.append(list(map(int, list(line))))

    grid = build_5x_grid(grid)

    q: List[Tuple[int, int, int]] = [(0, 0, 0)]  # total_risk, x, y
    risks: Dict[Tuple[int, int], int] = dict()

    m, n = len(grid) - 1, len(grid[0]) - 1

    while (m, n) not in risks:
        total, x, y = heapq.heappop(q)

        for dir in DIRECTIONS:
            newx, newy = x + dir[0], y + dir[1]
            if (
                0 <= newx < len(grid)
                and 0 <= newy < len(grid[0])
                and (newx, newy) not in risks
            ):
                risks[(newx, newy)] = total + grid[newx][newy]
                heapq.heappush(q, (risks[(newx, newy)], newx, newy))

    return risks[(m, n)]


if __name__ == "__main__":
    print(lowest_risk_path())
