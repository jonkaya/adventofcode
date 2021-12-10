from collections import defaultdict

INPUT_FILE_NAME = "input"


def optimum_crab_position() -> int:
    
    heights: List[int]
    
    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            
            heights = list(map(int, line.split(',')))
    
    dp: List[int] = [0 for _ in range(max(heights)+1)]
    
    for height in heights:
        for i in range(len(dp)):
            dp[i] += abs(height-i)

    return min(dp)


if __name__ == "__main__":
    print(optimum_crab_position())
