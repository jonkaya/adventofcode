import math

from collections import defaultdict
from typing import List, Tuple

INPUT_FILE_NAME = "input"

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
MAX_NUM = 9

def get_value_at_index(grid: List[List[int]], x: int, y: int) -> int:
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y]
    else:
        return MAX_NUM

def process_row(grid: List[List[int]], row_id: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = list()

    for i, val in enumerate(grid[row_id]):
        is_min = True
        for dir in DIRECTIONS:
            newx, newy = row_id+dir[0], i+dir[1]
            if val >= get_value_at_index(grid, newx, newy):
                is_min = False
                break
        if is_min:
            result.append((row_id, i))

    return result

def basin_bfs(grid: List[List[int]], point: Tuple[int, int]) -> int:
    # bfs in the grid and return the size of basin

    q: List[Tuple[int, int]] = list([point])
    basin: Set[Tuple[int, int]] = set()
    while q: 
        current_point = q.pop(0)
        basin.add(current_point)

        for dir in DIRECTIONS:
            newx, newy = dir[0]+current_point[0], dir[1]+current_point[1]
            if (newx, newy) not in basin and get_value_at_index(grid, newx, newy) != MAX_NUM:
                q.append((newx, newy))

    return len(basin)

def low_points() -> int:
    grid: List[List[int]] = list()
    low_pts: List[Tuple[int, int]] = list()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
            
            row = list(map(int, list(line)))
            grid.append(row)

    for i in range(len(grid)):
        low_pts.extend(process_row(grid, i))

    basins: List[int] = list()

    for point_tuple in low_pts:
        basins.append(basin_bfs(grid, point_tuple))

    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]

if __name__ == "__main__":
    print(low_points())
