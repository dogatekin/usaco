"""
ID: dotekin1
LANG: PYTHON3
TASK: combo
"""
from itertools import product

with open("combo.in") as fin:
    N = int(fin.readline())
    john = list(map(int, fin.readline().split()))
    master = list(map(int, fin.readline().split()))

combs = set()
for key in (john, master):
    opts = []
    for dial in key:
        opt = [(dial + d) % N for d in range(-2, 3)]
        opts.append(opt)
    combs |= set(product(*opts))
    
out = len(combs)
with open("combo.out", "w") as fout:
    fout.write(f"{out}\n")
