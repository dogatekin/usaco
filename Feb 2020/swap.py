from collections import defaultdict

with open('swap.in') as f:
    N, K = map(int, f.readline().split())
    A1, A2 = map(lambda x: int(x)-1, f.readline().split())
    B1, B2 = map(lambda x: int(x)-1, f.readline().split())
    
# if B2 < A2:
#     A1, A2, B1, B2 = B1, B2, A1, A2    
    
cows = list(range(1, N+1))

if K < 1000:
    for _ in range(K):
        cows[A1:A2+1] = reversed(cows[A1:A2+1])
        cows[B1:B2+1] = reversed(cows[B1:B2+1])
    out = cows
else:
    deltas = [0] * N
    b_deltas = [0] * N

    for i in range(B2-B1+1):
        deltas[B1+i] = B2 - B1 - 2*i
        b_deltas[B1+i] = B2 - B1 - 2*i

    for i in range(A2-A1+1):
        deltas[A1+i] = A2 - A1 - 2*i + b_deltas[A2 - i]

    print(deltas)

    locator = defaultdict(list)
    for i in range(min(A1, B1), max(A2,B2)+1):
        # print(i)
        locator[i].append(i)
        cur = i + deltas[i]
        
        while cur != i:
            locator[i].append(cur)
            cur = cur + deltas[cur]
        
    print(locator)

    out = cows[:]
    for cow, positions in locator.items():
        final = positions[K % len(positions)]
        out[final] = cows[cow]

with open('swap.out', 'w') as f:
    for cow in out:
        f.write(str(cow) + '\n')