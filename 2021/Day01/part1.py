

INPUT_FILE_NAME = "input"


def larger_than_previous() -> int:
    prev: Optional[int] = None
    increased: int = 0

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue

            val = int(line)

            if prev is not None and val > prev:
                increased += 1
                
            prev = val
    return increased


if __name__ == "__main__":
    print(larger_than_previous())