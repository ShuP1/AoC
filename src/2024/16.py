import sys
from heapq import heappop, heappush

B = [l.strip() for l in sys.stdin]

def find(v):
    return next((x, y) for y, l in enumerate(B)
                for x, c in enumerate(l) if c == v)
S, E = find('S'), find('E')

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
INF = float("inf")

best, paths = INF, set()
q, dists = [(0, S, 0, frozenset([S]))], {}
while q:
    c, p, d, path = heappop(q)
    if p == E:
        if c < best:
            best = c
            paths = path
        elif c == best:
            paths |= path
        continue

    k = p, d
    if dists.get(k, INF) < c:
        continue
    dists[k] = c

    x, y = p
    for od, a in ((0, 0), (1, 1000), (3, 1000), (2, 2000)):
        nd = (d + od) % 4
        dx, dy = DIRS[nd]
        np = nx, ny = x + dx, y + dy
        if B[ny][nx] != '#' and np not in path:
            heappush(q, (c + a + 1, np, nd, path | {np}))
print(best)
print(len(paths))
