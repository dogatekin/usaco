"""
ID: dotekin1
LANG: PYTHON3
TASK: beads
"""
def find_max(beads):
    m = 0
    c = 1
    changed = False
    cur = beads[0]
    whites = 0
    for bead in beads[1:]:
        if bead == cur:
            c += 1
            whites = 0
        elif bead == 'w':
            c += 1
            whites += 1
        elif not changed:
            c += 1
            cur = bead
            changed = True
            whites = 0
        else:
            c = whites + 1
            whites = 0
            changed = False
            cur = bead
        
        m = max(c, m)
        print(c, end='')
    
    return m

with open("beads.in") as fin:
    N, beads = fin.read().splitlines()

beads = beads + beads
for i, c in enumerate(beads):
    if c != 'w':
        break
beads = beads[i:] + beads[:i]

m1 = find_max(beads)

for i, c2 in enumerate(beads):
    if c2 != 'w' and c2 != c:
        break
beads = beads[i:] + beads[:i]

m2 = find_max(beads)

out = min(int(N), max(m1, m2))

with open("beads.out", "w") as fout:
    fout.write(f"{out}\n")
