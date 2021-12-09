from collections import defaultdict

INPUT_FILE_NAME = "input"


def binary_diagnose() -> int:
    
    total_lines: int = 0
    count_ones: Dict[int, int] = defaultdict(int)

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            if not line:
                continue
        
            for i, ch in enumerate(line):
                if ch == "1":
                    count_ones[i] += 1
            
            total_lines += 1
    
    gamma_rate: int = 0
    epsilon_rate: int = 0
    
    for i in range(len(count_ones)):
        factor = len(count_ones) - i - 1

        if count_ones[i] > total_lines//2:
            gamma_rate += 2**factor
        else:
            epsilon_rate += 2**factor

    return gamma_rate * epsilon_rate

if __name__ == "__main__":
    print(binary_diagnose())
