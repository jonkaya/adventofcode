from collections import defaultdict

INPUT_FILE_NAME = "input"


def squid_bingo_last_winner() -> int:
    
    boards: Dict[int, Dict[str, Dict[List[List[str]]]]] = defaultdict(lambda : defaultdict(list))

    numbers: List[str] = None
    counter: int = 0

    with open(INPUT_FILE_NAME) as input:
        for line in input.readlines():
            line = line.strip()
        
            if numbers is None:
                numbers = line.split(",")
            else:
                if not line:
                    counter += 1
                    continue
                row = line.split()
                boards[counter]["rows"].append(row)
                while len(boards[counter]["cols"]) < 5:
                    boards[counter]["cols"].append([])
                for i, num in enumerate(row):
                    boards[counter]["cols"][i].append(num)
                    boards[counter]["nums"].append(num)
    
    winning_boards: Dict[int, int] = dict()
    last_board_id: int = 0

    for draw in numbers:
        for board_id, board in boards.items():
            if draw in board["nums"]:
                boards[board_id]["nums"].remove(draw)
                for i in range(len(boards[board_id]["rows"])):
                    if draw in boards[board_id]["rows"][i]:
                        boards[board_id]["rows"][i].remove(draw)
                    if draw in boards[board_id]["cols"][i]:
                        boards[board_id]["cols"][i].remove(draw)

                    if len(boards[board_id]["rows"][i]) == 0 or len(boards[board_id]["cols"][i]) == 0:
                        if board_id not in winning_boards:
                            winning_boards[board_id] = sum([int(n) for n in boards[board_id]["nums"]]) * int(draw)
                            last_board_id = board_id
    
    return winning_boards[last_board_id]

if __name__ == "__main__":
    print(squid_bingo_last_winner())
