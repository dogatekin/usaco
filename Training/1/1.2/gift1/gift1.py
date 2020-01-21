"""
ID: dotekin1
LANG: PYTHON3
TASK: gift1
"""
with open('gift1.in') as fin:
    lines = fin.read().splitlines()
    
NP = int(lines[0])
money = {name: 0 for name in lines[1:NP+1]}

giver_line = NP + 1
while giver_line < len(lines):
    giver = lines[giver_line]
    amount, people = map(int, lines[giver_line+1].split())
    
    if people > 0:
        each = amount // people
        rem = amount % people
        
        money[giver] -= amount - rem
        
        for person in lines[giver_line+2:giver_line+2+people]:
            money[person] += each
    
    giver_line = giver_line + people + 2
    
with open('gift1.out', 'w') as fout:
    for person, amount in money.items():
        fout.write(f'{person} {amount}\n')