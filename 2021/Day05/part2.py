from collections import defaultdict

INPUT_FILE_NAME = "input"


def hydrothermal_venture_diagonal() -> int:
    
    coords: Dict[Tuple[int, int], int] = defaultdict(int)
    
    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
        
            parts = line.split(" -> ")
            assert len(parts) == 2

            x1, y1 = parts[0].split(",")
            x2, y2 = parts[1].split(",")

            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

            if x1 == x2:
                x = x1
                y_min, y_max = (y1, y2) if y2 > y1 else (y2, y1) 

                while y_min <= y_max:
                    coords[(x,y_min)] += 1
                    y_min += 1
            elif y1 == y2:
                y = y1
                x_min, x_max = (x1, x2) if x2 > x1 else (x2, x1)

                while x_min <= x_max:
                    coords[(x_min, y)] += 1
                    x_min += 1
            elif abs(x1 - x2) == abs(y1 - y2):
                dir_x = 1 if x2 > x1 else -1
                dir_y = 1 if y2 > y1 else -1

                while x1 != x2 and y1 != y2:
                    coords[(x1, y1)] += 1
                    x1 += dir_x
                    y1 += dir_y
                coords[(x2,y2)] += 1   

    return len(list(filter(lambda x: x > 1, coords.values())))



if __name__ == "__main__":
    print(hydrothermal_venture_diagonal())
