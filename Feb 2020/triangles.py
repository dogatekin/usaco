from collections import defaultdict

with open('triangles.in') as f:
    N = int(f.readline())
    posts = [tuple(map(int, line.split())) for line in f.read().splitlines()]
  
xs = defaultdict(list)
ys = defaultdict(list)
for x, y in posts:
    xs[x].append(y)
    ys[y].append(x)

ma = 0
for x1, potential_ys in xs.items():
    for i in range(len(potential_ys)):
        for j in range(i+1, len(potential_ys)):
            y1 = potential_ys[i]
            y2 = potential_ys[j]
            for x2 in ys[y1] + ys[y2]:
                a = abs(x1 - x2) * abs(y1 - y2)
                ma = max(a, ma)

with open('triangles.out', 'w') as f:
    f.write(str(ma) + '\n')