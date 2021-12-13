
from typing import Dict, List, Set, Tuple

INPUT_FILE_NAME = "input"


class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()

def dfs(nodes: Dict[str, Node], start: str, end: str, path:Tuple[str], visited: Dict[str, bool], visited_lower=False) -> int:
    all_paths: Set[Tuple[str]] = set()
    if start == end:
        all_paths.add(path)
        return all_paths

    # only lower caves can be visited once
    if start.islower():
        visited[start] = True

    for neighbor in nodes[start].children:
        if neighbor.val not in visited:
            new_visited = {k: v for k, v in visited.items()}
            all_paths.update(dfs(nodes, neighbor.val, end, tuple(list(path) + [neighbor.val]), new_visited, visited_lower))
        elif neighbor.val.islower() and visited_lower is False and neighbor.val != "start":
            # allow a lower node to be visited once more
            new_visited = {k: v for k, v in visited.items()}
            all_paths.update(dfs(nodes, neighbor.val, end, tuple(list(path) + [neighbor.val]), new_visited, visited_lower=True))

    return all_paths

def distinct_paths() -> int:
    nodes: Dict[str, Node] = dict()

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()

            orig, term = line.split("-")
            if orig not in nodes:
                nodes[orig] = Node(val=orig)
            if term not in nodes:
                nodes[term] = Node(val=term)
            nodes[orig].children.add(nodes[term])
            nodes[term].children.add(nodes[orig])

    all_paths = dfs(nodes, "start", "end", ("start",), dict())

    return len(all_paths)

if __name__ == "__main__":
    print(distinct_paths())
