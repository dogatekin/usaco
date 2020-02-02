"""
ID: dotekin1
LANG: PYTHON3
TASK: milk2
"""
from itertools import accumulate
from collections import defaultdict, OrderedDict

with open("milk2.in") as fin:
    N = fin.readline()
    farmers = [line.strip().split(' ') for line in fin.readlines()]

cows = defaultdict(int)

for start, end in farmers:
    cows[int(start)] += 1
    cows[int(end)] -= 1
    
print(cows)

# cur = 0
start_milk = None
max_milk = max_none = 0

sorted_cows = sorted(cows.items())
start_milk, cur = sorted_cows[0]
print(start_milk, cur)
for t, change in sorted_cows[1:]:    
    cur += change
    print(t, cur)
    
    if cur == 0 and start_milk is not None:
        milk_time = t - start_milk
        max_milk = max(milk_time, max_milk)
        start_milk = None
        start_none = t
    elif cur != 0 and start_milk is None:
        none_time = t - start_none
        max_none = max(none_time, max_none)
        start_milk = t

with open("milk2.out", "w") as fout:
    fout.write(f"{max_milk} {max_none}\n")
