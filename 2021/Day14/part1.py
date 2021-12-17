from collections import defaultdict
from typing import Dict, List

INPUT_FILE_NAME = "input"

ITERATION_COUNT = 10


def split_pairs(s: str) -> List[str]:
    pairs: List[str] = list()

    for i in range(len(s) - 1):
        pairs.append(s[i : i + 2])

    return pairs


def polymer_insert() -> int:
    rules: Dict[str, str] = dict()
    polymer_template: str = None

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue

            if polymer_template is None:
                polymer_template = line
            if "->" in line:
                key, val = line.split(" -> ")
                # BN -> B becomes BN: BB removing the last char
                # because we will get it from the next pair's first element
                rules[key] = f"{key[0]}{val}"

    for _ in range(ITERATION_COUNT):
        pairs = split_pairs(polymer_template)

        for i in range(len(pairs)):
            if pairs[i] in rules:
                pairs[i] = rules[pairs[i]]

        polymer_template = (
            "".join(pairs) + polymer_template[-1]
        )  # append the last char we initially removed in rules

    counter: Dict[str, int] = defaultdict(int)

    for c in polymer_template:
        counter[c] += 1

    return max(counter.values()) - min(counter.values())


if __name__ == "__main__":
    print(polymer_insert())
