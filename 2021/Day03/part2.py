from collections import defaultdict
from typing import List

INPUT_FILE_NAME = "input"

def split_by_index(rows: List[str], index: int = 0) -> List[List[str]]:
    zeros: List[str] = list()
    ones: List[str] = list()

    if len(rows) == 1:
        return [rows, rows]

    for row in rows:
        if row[index] == "0":
            zeros.append(row)
        elif row[index] == "1":
            ones.append(row)

    return [zeros, ones] if len(zeros) > len(ones) else [ones, zeros]


def life_support_rating() -> int:
    
    rows: List[str] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue
            rows.append(line)

    most_common = [row for row in rows]
    least_common = [row for row in rows]

    for i in range(len(rows[0])):
        most_common, _ = split_by_index(most_common, i)
        _, least_common = split_by_index(least_common, i)

    assert len(most_common) == 1
    assert len(least_common) == 1

    o2_generator_rating: int = 0
    co2_scrubber_rating: int = 0

    for i in range(len(rows[0])):
        factor = len(rows[0]) - i - 1
    
        o2_generator_rating += int(most_common[0][i]) * 2**factor
        co2_scrubber_rating += int(least_common[0][i]) * 2**factor

    return o2_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
    print(life_support_rating())
