from collections import defaultdict

from typing import Dict, List

INPUT_FILE_NAME = "input"

"""
1: cf
7: acf
4: bcdf

2: acdeg
3: acdfg
5: abdfg

6: abdefg
0: abcefg
9: abcdfg

8: abcdefg

"""


def seven_segment_decoder(input: List[str], numbers: List[str]) -> List[int]:

    input = sorted(input, key=lambda x: len(x))
    mapping: Dict[int, str] = dict()
    signals: Dict[str, int] = dict()

    # pop input for 8
    mapping[8] = input.pop()

    mapping[1] = input.pop(0)
    mapping[7] = input.pop(0)
    mapping[4] = input.pop(0)

    top_signal = set(list(mapping[7])).difference(set(list(mapping[1]))).pop()

    # find 9
    four_and_seven = set(mapping[4] + mapping[7])
    for i in range(len(input) - 1, len(input) - 4, -1):
        diff = set(input[i]).difference(four_and_seven)
        if len(diff) == 1:
            mapping[9] = input[i]
            input.pop(i)
            break

    left_bottom = set(list(mapping[8])).difference(set(list(mapping[9]))).pop()

    # find 2
    for i in range(3):
        if left_bottom in input[i]:
            mapping[2] = input[i]
            input.pop(i)
            break

    three_and_five = input[:2]
    zero_and_six = input[2:]

    found: bool = False

    for i in range(len(zero_and_six)):
        num1 = zero_and_six[i]
        for j in range(len(three_and_five)):
            num2 = three_and_five[j]
            diff = set(list(num1)).difference(set(list(num2)))
            # only 5 and 6 has 1 segment difference
            if len(diff) == 1:
                mapping[6] = num1
                mapping[5] = num2
                zero_and_six.remove(num1)
                three_and_five.remove(num2)
                mapping[0] = zero_and_six[0]
                mapping[3] = three_and_five[0]
                found = True
                break
        if found:
            break

    for digit, signal in mapping.items():
        signals["".join(sorted(signal))] = digit

    return [signals["".join(sorted(signal))] for signal in numbers]


def seven_segment_search() -> int:

    number_occurances: Dict[int, int] = defaultdict(int)

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            inputs, results = line.split(" | ")

            numbers = seven_segment_decoder(inputs.split(), results.split())
            for num in numbers:
                number_occurances[num] += 1

    return sum([number_occurances[num] for num in (1, 4, 7, 8)])


if __name__ == "__main__":
    print(seven_segment_search())
