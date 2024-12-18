import sys
from collections import deque

B = [tuple(map(int, l.strip().split(','))) for l in sys.stdin]
S = max(map(max, B))

def sim(n):
    grid = set(B[:n])
    q = deque([(0, 0, 0)])
    seen = set()
    while q:
        x, y, d = q.popleft()
        if (x, y) == (S, S):
            return d
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx <= S and 0 <= ny <= S and (nx, ny) not in grid:
                q.append((nx, ny, d + 1))
print(sim(1024 if S > 6 else 12))

l, r = 0, len(B)
while l < r:
    m = (l + r) // 2
    if not sim(m):
        r = m
    else:
        l = m + 1
print(*B[l-1], sep=',')
