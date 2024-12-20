import sys
from collections import deque

B = [l.strip() for l in sys.stdin]
S = next((x, y) for y, l in enumerate(B)
        for x, c in enumerate(l) if c == 'S')

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
INF = float("inf")

q, dists = deque([(0, S)]), {}
while q:
    c, p = q.popleft()
    if dists.get(p, INF) <= c:
        continue
    dists[p] = c

    x, y = p
    for dx, dy in DIRS:
        np = nx, ny = x + dx, y + dy
        if B[ny][nx] != '#':
            q.append((c + 1, np))

n2 = n20 = 0
for (x1, y1), d1 in dists.items():
    for (x2, y2), d2 in dists.items():
        diff = int(abs(x2-x1) + abs(y2-y1))
        if d1 - d2 - diff >= 100:
            n2 += diff <= 2
            n20 += diff <= 20
print(n2)
print(n20)
