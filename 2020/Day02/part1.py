

def part1():
    validCount = 0
    with open("input", "r") as f:
        line = f.readline()
        while line:
            minmax, c, passwd = line.split()
            min_num, max_num = minmax.split("-")
            c = c[:-1]

            actual = passwd.count(c)
            if int(min_num) <= actual <= int(max_num):
                validCount += 1
            line = f.readline()
    print(validCount)


if __name__ == "__main__":
    part1()
