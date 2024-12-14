import sys
from math import prod
from itertools import count

B = [tuple(tuple(map(int, p[2:].split(',')))
    for p in l.split()) for l in sys.stdin]

X = max(v[0][0] for v in B)+1
Y = max(v[0][1] for v in B)+1

def move(b, t):
    (x,y),(vx,vy) = b
    x = (x+vx*t) % X
    y = (y+vy*t) % Y
    return x, y

quad = [0] * 4
for b in B:
    x,y = move(b, 100)
    qx, qy = x-X//2, y-Y//2
    if qx and qy:
        quad[2*(qx>0)+(qy>0)] += 1
print(prod(quad))

PS0 = set(p for p, _ in B)
ps = set()
best = 0, 0
for t in count(1):
    ps = {move(b, t) for b in B}
    if ps == PS0:
        break

    density = sum((x+dx, y+dy) in ps for x, y in ps
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)))
    if density > best[0]:
        best = density, t
print(best[1])
