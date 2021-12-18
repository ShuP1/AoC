import sys
from collections import deque

FAV = int(sys.stdin.readline())
def is_open(x, y):
    if x < 0 or y < 0:
        return False
    v = x*x + 3*x + 2*x*y + y + y*y + FAV
    return bin(v).count('1') % 2 == 0

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def path(T, limit=float('inf')):
    close = set([(1, 1)])
    queue = deque([(1, 1, 0)])
    while queue:
        x, y, steps = queue.popleft()
        steps += 1
        if steps > limit:
            return False, len(close)
        for dx, dy in DIRS:
            p = (x + dx, y + dy)
            if p == T:
                return True, steps
            if p not in close and is_open(*p):
                close.add(p)
                queue.append((*p, steps))

print(path((31, 39))[1])
print(path(None, 50)[1])
