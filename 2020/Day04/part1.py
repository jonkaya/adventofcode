import re

VALID_FIELDS = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}

OPTIONAL_FIELDS = {"cid"}

VALID_EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def check_field(field):
    field_name, value = field.split(":")
    check_method = {
        "byr": lambda x: len(x) == 4 and 2002 >= int(x) >= 1920,
        "iyr": lambda x: len(x) == 4 and 2020 >= int(x) >= 2010,
        "eyr": lambda x: len(x) == 4 and 2030 >= int(x) >= 2020,
        "hgt": lambda x: (x.endswith("in") and 76 >= int(x[:-2]) >= 59) or (x.endswith("cm") and 193 >= int(x[:-2]) >= 150),
        "hcl": lambda x: len(x) == 7 and re.match("#[0-9A-Fa-f]{6}", x) is not None,
        "ecl": lambda x: x in VALID_EYE_COLORS,
        "pid": lambda x: re.match("^[0-9]{9}$", x) is not None,
        "cid": lambda x: True,
    }
    return check_method[field_name](value)


def part1():
    input_list = []

    with open("input", "r") as f:
        buffer = f.readline()
        previous_buffer = ""
        item = ""
        while buffer != previous_buffer:
            item += buffer.replace("\n", " ")
            if buffer == "\n":
                input_list.append(item.strip())
                item = ""
            previous_buffer = buffer
            buffer = f.readline()

    valid_count = 0

    for input in input_list:
        if all([
            x in input for x in VALID_FIELDS
        ]):
            valid_count += 1

    print(valid_count)

if __name__ == "__main__":
    part1()
