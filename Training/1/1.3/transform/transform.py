"""
ID: dotekin1
LANG: PYTHON3
TASK: transform
"""
def rotate_90(matrix):
    N = len(matrix)
    return [[matrix[N-j-1][i] for j in range(N)] for i in range(N)]

def rotate_180(matrix):
    return rotate_90(rotate_90(matrix))

def rotate_270(matrix):
    return rotate_180(rotate_90(matrix))

def reflect(matrix):
    return [list(reversed(row)) for row in matrix]

with open("transform.in") as fin:
    N = int(fin.readline())
    lines = fin.read().splitlines()

before = [list(line) for line in lines[:N]]
after = [list(line) for line in lines[N:]]

if rotate_90(before) == after:
    out = 1
elif rotate_180(before) == after:
    out = 2
elif rotate_270(before) == after:
    out = 3
else:
    reflected = reflect(before)
    if reflected == after:
        out = 4
    elif rotate_90(reflected) == after:
        out = 5
    elif rotate_180(reflected) == after:
        out = 5
    elif rotate_270(reflected) == after:
        out = 5
    elif before == after:
        out = 6
    else:
        out = 7

with open("transform.out", "w") as fout:
    fout.write(f"{out}\n")
