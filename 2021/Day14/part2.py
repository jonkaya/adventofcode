from collections import defaultdict
from typing import Dict

INPUT_FILE_NAME = "input"

ITERATION_COUNT = 40


def polymer_insert() -> int:
    rules: Dict[str, str] = dict()
    polymer_template: str = None

    char_counter: Dict[str, int] = defaultdict(int)
    pair_counts: Dict[str, int] = defaultdict(int)

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue

            if polymer_template is None:
                polymer_template = line
            if "->" in line:
                key, val = line.split(" -> ")
                rules[key] = val

    for i in range(len(polymer_template) - 1):
        pair_counts[polymer_template[i : i + 2]] += 1
        char_counter[polymer_template[i]] += 1
    char_counter[polymer_template[-1]] += 1

    for _ in range(ITERATION_COUNT):
        pair_counts_per_iteration: Dict[str, int] = defaultdict(int)

        for pair, pair_count in pair_counts.items():
            if pair in rules:
                pair_counts_per_iteration[f"{pair[0]}{rules[pair]}"] += pair_count
                pair_counts_per_iteration[f"{rules[pair]}{pair[1]}"] += pair_count
                char_counter[rules[pair]] += pair_count
        pair_counts = pair_counts_per_iteration

    return max(char_counter.values()) - min(char_counter.values())


if __name__ == "__main__":
    print(polymer_insert())
