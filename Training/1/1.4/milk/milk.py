"""
ID: dotekin1
LANG: PYTHON3
TASK: milk
"""
with open("milk.in") as fin:
    milk_to_get, n = map(int, fin.readline().split())
    farmers = [list(map(int, line.split())) for line in fin.readlines()]

spent = 0
for price, units in sorted(farmers, key=lambda pair: pair[0]):
    if milk_to_get <= units:
        spent += milk_to_get * price
        break
    else:
        milk_to_get -= units
        spent += units * price
        
with open("milk.out", "w") as fout:
    fout.write(f"{spent}\n")
