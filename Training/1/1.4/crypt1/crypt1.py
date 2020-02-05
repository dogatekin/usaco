"""
ID: dotekin1
LANG: PYTHON3
TASK: crypt1
"""
from itertools import product

def check_digits(n, digits):
    for char in str(n):
        if char not in digits:
            return False
    return True

with open("crypt1.in") as fin:
    N = int(fin.readline())
    digits = list(sorted(map(int, fin.readline().split())))

smalls = list(product(digits, digits))
larges = list(product(digits, digits, digits))
digits = set(map(str, digits))

out = 0
for small in smalls:
    for large in larges:
        large = large[0]*100 + large[1]*10 + large[2]
        
        partial1 = small[1] * large
        if partial1 > 999: 
            break
        if not check_digits(partial1, digits):
            continue
        
        partial2 = small[0] * large
        if partial2 > 999: 
            break
        if not check_digits(partial2, digits):
            continue
        
        total = partial2*10 + partial1
        if total > 9999:
            break
        if not check_digits(total, digits):
            continue
        
        out += 1

with open("crypt1.out", "w") as fout:
    fout.write(f"{out}\n")
