"""
ID: dotekin1
LANG: PYTHON3
TASK: skidesign
"""
from itertools import accumulate

with open("skidesign.in") as fin:
    N = int(fin.readline())
    hills = list(sorted(map(int, fin.read().splitlines())))

diff = hills[-1] - hills[0]
delta = diff - 17

out = 0

if delta > 0:
    costs = []
    for inc in range(delta+1):
        dec = delta - inc
        
        lo = hills[0] + inc
        hi = hills[-1] - dec
        
        cost = 0
        for hill in hills:
            if hill < lo:
                cost += (lo - hill)**2
            elif hill > hi:
                cost += (hill - hi)**2
        costs.append(cost)
    out = min(costs)
    
with open("skidesign.out", "w") as fout:
    fout.write(f"{out}\n")
