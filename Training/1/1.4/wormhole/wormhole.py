"""
ID: dotekin1
LANG: PYTHON3
TASK: wormhole
"""
def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    
    a = lst[0]
    for i in range(1,len(lst)):
        pair = (a,lst[i])
        for rest in all_pairs(lst[1:i]+lst[i+1:]):
            yield [pair] + rest
  
def check_loop(wormholes, portals, start):
    next_wormhole = start
    
    while next_wormhole:
        cur = portals[next_wormhole]
        aligned_wormholes = list(filter(lambda w: w[1] == cur[1] and w[0] > cur[0], wormholes))
        if len(aligned_wormholes) == 0:
            return False
        next_wormhole = min(aligned_wormholes, key=lambda w: w[0])
        if next_wormhole == start:
            return True
                
with open("wormhole.in") as fin:
    N = int(fin.readline())
    lines = fin.read().splitlines()

wormholes = [tuple(map(int, line.split())) for line in lines]

out = 0
for pairing in all_pairs(wormholes):
    portals = {}

    for a, b in pairing:
        portals[a] = b
        portals[b] = a
        
    for start in wormholes:
        if check_loop(wormholes, portals, start):
            out += 1
            break

with open("wormhole.out", "w") as fout:
    fout.write(f"{out}\n")
