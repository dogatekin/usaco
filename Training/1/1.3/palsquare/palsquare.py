"""
ID: dotekin1
LANG: PYTHON3
TASK: palsquare
"""
def base_10_to_b(num, b):
    if num == 0:
        return '0'
    
    out = ''
    while num:
        mod = num % b
        num //= b
        out = chr(ord('0') + mod + (ord('A') - ord('0') - 10)*(mod >= 10)) + out
    return out

def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[len(text)-i-1]:
            return False
    return True

with open("palsquare.in") as fin:
    B = int(fin.read())

out = []
for i in range(1, 301):
    in_base_sq = base_10_to_b(i*i, B)
    if is_palindrome(in_base_sq):
        out.append((base_10_to_b(i, B), in_base_sq))

with open("palsquare.out", "w") as fout:
    for i, i_sq in out:
        fout.write(f"{i} {i_sq}\n")
