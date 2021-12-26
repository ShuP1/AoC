import sys
from typing import Coroutine

COORDS = {(*map(int,line.split(', ')),) for line in sys.stdin.readlines()}
LIMIT = 10000

def fill(p, when, limit=False):
    close = set([p])
    queue = [p]
    while queue and (not limit or len(close) < limit):
        x, y = queue.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            q = x+dx, y+dy
            if q not in close and when(q):
                close.add(q)
                queue.append(q)
    return len(close) if not queue else -1

def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def nearest(p):
    others = COORDS - {p}
    return lambda q: dist(p, q) < min(dist(o, q)
        for o in others)
print(max(fill(p, nearest(p), LIMIT) for p in COORDS))

def safe(p):
    return sum(dist(p, q) for q in COORDS) < LIMIT
print(fill(next(filter(safe, COORDS)), safe))
