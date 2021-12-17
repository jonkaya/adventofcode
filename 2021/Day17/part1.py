import math
from typing import List, Tuple

INPUT_FILE_NAME = "input"


def move_step(
    position: Tuple[int, int], velocity: Tuple[int, int]
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    v_x, v_y = velocity

    new_x, new_y = position[0] + v_x, position[1] + v_y

    if v_x > 0:
        v_x -= 1
    elif v_x < 0:
        v_x += 1
    v_y -= 1
    return ((new_x, new_y), (v_x, v_y))


def simulate_shot(
    velocity: Tuple[int, int], target: Tuple[int]
) -> List[Tuple[int, int]]:

    position: Tuple[int, int] = (0, 0)
    x_min, x_max, y_min, y_max = target
    path: List[Tuple[int, int]] = list()

    while position[0] <= x_max and position[1] >= y_min:
        path.append(position)
        position, velocity = move_step(position, velocity)

        if x_min <= position[0] <= x_max and y_min <= position[1] <= y_max:
            return path

    return list()


def trick_shot() -> int:

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue
            # target area: x=253..280, y=-73..-46
            line = line.strip("target area: ")
            x_range, y_range = line.split(", ")
            x_range = x_range.lstrip("x=")
            y_range = y_range.lstrip("y=")

            x_min, x_max = list(map(int, x_range.split("..")))
            y_min, y_max = list(map(int, y_range.split("..")))

    max_height = -math.inf

    for v_x in range(x_min, 1, -1):
        for v_y in range(1000):
            path = simulate_shot((v_x, v_y), (x_min, x_max, y_min, y_max))
            if path:
                max_height = max(max_height, max([p[1] for p in path]))

    return max_height


if __name__ == "__main__":
    print(trick_shot())
