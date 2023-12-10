import sys
from itertools import count

M = [l.strip() for l in sys.stdin.readlines()]
# n, e, s, w
D = [(0, -1), (1, 0), (0, 1), (-1, 0)]
P = {
    '|': (0, 2),
    '-': (1, 3),
    'L': (0, 1),
    'J': (0, 3),
    '7': (2, 3),
    'F': (2, 1),
    '.': (-1, -1)
}
def get(x,y): return M[y][x] if 0 <= y < len(M) and 0 <= x < len(M[y]) else '.'
def swap(d): return (d+2)%4

x, y = next((l.find('S'),y) for y,l in enumerate(M) if 'S' in l)
d = next(d for d, (dx, dy) in enumerate(D) if swap(d) in P[get(x+dx, y+dy)])
ps = set()
for p1 in count(1):
    ps.add((x, y))
    x += D[d][0]
    y += D[d][1]
    c = get(x,y)
    if c == 'S':
        break
    p = P[c]
    d = p[p[0] == swap(d)]
print(len(ps) // 2)

p2 = 0
for y, r in enumerate(M):
    inside = False
    for x, p in enumerate(r):
        if (x,y) in ps:
            if p in "|JL":
                inside = not inside
        else:
            p2 += inside
print(p2)
