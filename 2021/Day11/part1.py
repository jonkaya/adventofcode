from typing import List, Set, Tuple

INPUT_FILE_NAME = "input"

NEIGHBORS = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1),
]

SIM_STEPS = 100


def simulate_one_step(rows: List[List[int]]) -> int:
    flash_count: int = 0
    flashed: Set[Tuple[int, int]] = set()

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            q: List[Tuple[int, int]] = list([(i, j)])

            while q:
                x, y = q.pop(0)
                if (x, y) in flashed:
                    continue
                if rows[x][y] == 9:
                    flash_count += 1
                    flashed.add((x, y))
                    rows[x][y] = 0
                    for dir in NEIGHBORS:
                        newx, newy = x + dir[0], y + dir[1]
                        if 0 <= newx < len(rows) and 0 <= newy < len(rows[0]):
                            q.append((newx, newy))
                else:
                    rows[x][y] += 1

    return flash_count


def dumbo_octopus() -> int:
    total_flashes: int = 0

    rows: List[List[int]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            row = list(map(int, line))
            rows.append(row)

    for _ in range(SIM_STEPS):
        total_flashes += simulate_one_step(rows)

    return total_flashes


if __name__ == "__main__":
    print(dumbo_octopus())
