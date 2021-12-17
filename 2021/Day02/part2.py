INPUT_FILE_NAME = "input"


def submarine_position() -> int:
    horizontal: int = 0
    depth: int = 0

    aim: int = 0

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue

            direction, val = line.split()

            if direction == "forward":
                horizontal += int(val)
                depth += aim * int(val)
            elif direction == "up":
                aim -= int(val)
            elif direction == "down":
                aim += int(val)

    return horizontal * depth


if __name__ == "__main__":
    print(submarine_position())
