with open('breedflip.in') as f:
    N = int(f.readline())
    A, B = f.read().splitlines()
    
count = 0
cur_unmatched = False
for a, b in zip(A, B):
    if a != b and not cur_unmatched:
        count += 1
        cur_unmatched = True
    elif a == b and cur_unmatched:
        cur_unmatched = False

with open('breedflip.out', 'w') as f:
    f.write(str(count) + '\n')