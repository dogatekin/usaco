"""
ID: dotekin1
LANG: PYTHON3
TASK: barn1
"""
def find_gap(cows):
    if len(cows) == 1:
        return 0, 0, 0
    
    gaps = [j - i for i, j in zip(cows[:-1], cows[1:])]
    largest_gap = max(range(len(gaps)), key=lambda i: gaps[i])
    return cows[largest_gap+1] - cows[largest_gap], largest_gap, largest_gap+1

def min_blocked(cows, num_boards):
    if num_boards == 1:
        return [(0, len(cows)-1)]
    
    cur_boards = min_blocked(cows, num_boards-1)
    
    gaps = []
    for i, board in enumerate(cur_boards):
        start, end = board
        gap_size, s, e = find_gap(cows[start:end+1])
        gaps.append((i, (gap_size, start+s, start+e)))

    board_ind, gap = max(gaps, key=lambda gap: gap[1])
    old_start, old_end = cur_boards.pop(board_ind)
    cur_boards.append((old_start, gap[1]))
    cur_boards.append((gap[2], old_end))
    
    return cur_boards

with open("barn1.in") as fin:
    M, S, C = map(int, fin.readline().split())
    cows = sorted(list(map(int,fin.read().splitlines())))

if M > C:
    M = C
    
boards = min_blocked(cows, M)
out = sum(cows[end] - cows[start] + 1 for start, end in boards)

with open("barn1.out", "w") as fout:
    fout.write(f"{out}\n")
