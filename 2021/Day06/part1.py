from typing import List

INPUT_FILE_NAME = "input"

SIM_DAYS = 80


def lantern_fish_sim() -> int:

    fish_timer: List[int]

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            fish_timer = list(map(int, line.split(",")))

    for day in range(SIM_DAYS):
        new_fish: List[int] = list()

        for i in range(len(fish_timer)):
            if fish_timer[i] == 0:
                fish_timer[i] = 6
                new_fish.append(8)
            else:
                fish_timer[i] -= 1

        if new_fish:
            fish_timer.extend(new_fish)

    return len(fish_timer)


if __name__ == "__main__":
    print(lantern_fish_sim())
