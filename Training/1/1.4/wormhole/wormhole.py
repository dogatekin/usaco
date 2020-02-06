"""
ID: dotekin1
LANG: PYTHON3
TASK: wormhole
"""
def gen_pairings(xs):
    if len(xs) == 2:
        return [[(xs[0], xs[1])]]
    
    pairings = []
    for i in range(1, len(xs)):
        pair = (xs[0], xs[i])
        for rest in gen_pairings(xs[1:i] + xs[i+1:]):
            pairings.append([pair] + rest)
    
    return pairings
 
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
for pairing in gen_pairings(wormholes):
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
