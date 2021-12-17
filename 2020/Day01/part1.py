def part1():
    mapping = dict()

    with open("input", "r") as f:
        arr = f.read().split()

    for i in arr:
        complement = 2020 - int(i)
        if complement in mapping:
            print(int(i) * complement)
        mapping[int(i)] = 1


if __name__ == "__main__":
    part1()
