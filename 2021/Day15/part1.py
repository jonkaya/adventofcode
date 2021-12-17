import heapq

from typing import Dict, List, Set, Tuple

INPUT_FILE_NAME = "input"

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

def lowest_risk_path() -> int:
    grid: List[List[int]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            if not line:
                continue
            grid.append(list(map(int, list(line))))

    # !! Too slow
    # def dfs(current_pos: Tuple[int, int], path: List[Tuple[int, int]], total: int):
    #     min_risk: int = math.inf
    #     x, y = current_pos

    #     if x == len(grid)-1 and y == len(grid[0])-1:
    #         return total

    #     for dir in DIRECTIONS:
    #         newx, newy = x+dir[0], y+dir[1]
    #         if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in path:
    #             path.append((newx, newy))
    #             min_risk = min(min_risk, dfs((newx, newy), path, total+grid[x][y]))
    #             path.remove((newx, newy))
    #     return min_risk
    # return dfs((0,0), [(0,0)], 0, dict())

    q: List[Tuple[int, int, int]] = [(0, 0, 0)] # total_risk, x, y
    risks: Dict[Tuple[int, int], int] = dict()

    m, n = len(grid)-1, len(grid[0])-1

    while (m,n) not in risks:
        total, x, y = heapq.heappop(q)

        for dir in DIRECTIONS:
            newx, newy = x+dir[0], y+dir[1]
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx,newy) not in risks:
                risks[(newx,newy)] = total + grid[newx][newy]
                heapq.heappush(q, (risks[(newx,newy)], newx, newy))

    return risks[(m,n)]

if __name__ == "__main__":
    print(lowest_risk_path())
