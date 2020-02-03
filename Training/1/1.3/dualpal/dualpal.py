"""
ID: dotekin1
LANG: PYTHON3
TASK: dualpal
"""
def base_10_to_b(n, b):
    if not n:
        return '0'
    
    out = ''
    while n:
        mod = n % b
        n //= b
        out = chr(48 + mod + 7*(mod >= 10)) + out
    return out
    
def count(n):
    while True:
        yield n
        n += 1
        
def is_palindrome(n):
    for i in range(len(n) // 2):
        if n[i] != n[len(n)-i-1]:
            return False
    return True
            
with open("dualpal.in") as fin:
    N, S = map(int, fin.read().split())

out = []
for i in count(S+1):
    palindrome_in = 0
    
    for b in range(2, 11):
        if is_palindrome(base_10_to_b(i, b)):
            palindrome_in += 1
            if palindrome_in == 2:
                out.append(i)
                break
    
    if len(out) == N:
        break

with open("dualpal.out", "w") as fout:
    for o in out:
        fout.write(f"{o}\n")
