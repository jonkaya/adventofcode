

def part2():

    with open("input", "r") as f:
        arr = f.read().split()

    for i in arr:
        mapping = dict()
        total = 2020 - int(i)
        for j in arr:
            complement = total - int(j)
            if complement in mapping:
                print(int(i) * int(j) * complement)
            mapping[int(j)] = 1


if __name__ == "__main__":
    part2()
