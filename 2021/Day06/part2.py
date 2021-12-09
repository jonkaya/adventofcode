from collections import defaultdict
from typing import List, Tuple

INPUT_FILE_NAME = "input"

SIM_DAYS = 256

def lantern_fish_counter() -> int:
    
    fish_counter: Dict[int, int] = defaultdict(int)

    
    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            
            fish_timer = list(map(int, line.split(',')))
    

    for fish in fish_timer:
        fish_counter[fish] += 1

    for day in range(SIM_DAYS):
        zero_count = fish_counter[0]
        for i in range(1, 9):
            fish_counter[i-1] = fish_counter[i]
        fish_counter[6] += zero_count
        fish_counter[8] = zero_count
        
    return sum(fish_counter.values())


if __name__ == "__main__":
    print(lantern_fish_counter())
