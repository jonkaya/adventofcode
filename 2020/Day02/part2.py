
def part2():
    validCount = 0
    with open("input", "r") as f:
        line = f.readline()
        while line:
            minmax, c, passwd = line.split()
            min_num, max_num = minmax.split("-")
            c = c[:-1]

            firstIndex = passwd[int(min_num)-1] == c
            secondIndex = passwd[int(max_num)-1] == c

            if int(firstIndex) + int(secondIndex) == 1:
                validCount += 1
            line = f.readline()
    print(validCount)

if __name__ == "__main__":
    part2()
