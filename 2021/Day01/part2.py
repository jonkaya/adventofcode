from typing import List, Optional


INPUT_FILE_NAME = "input"


def larger_than_previous_window() -> int:
    prev: Optional[int] = None
    increased: int = 0
    window: List[int] = list()
    total: int = 0

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue

            val = int(line)

            window.append(val)
            total += val

            if len(window) > 3:
                to_remove = window.pop(0)
                total -= to_remove
            if len(window) == 3:
                if prev is not None and total > prev:
                    increased += 1

                prev = total
    return increased


if __name__ == "__main__":
    print(larger_than_previous_window())
