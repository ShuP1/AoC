import sys
from itertools import product
from functools import reduce
from operator import mul

GRID = [[*map(int, line.strip())] for line in sys.stdin.readlines()]
X, Y = len(GRID), len(GRID[0])

def ngb(sx, sy):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x, y = sx+dx, sy+dy
        if 0 <= x < X and 0 <= y < Y:
            yield (x, y)

lows = set()
risk = 0
for x, y in product(range(X), range(Y)):
    v = GRID[x][y]
    if all(map(lambda p: v < GRID[p[0]][p[1]], ngb(x, y))):
        lows.add((x, y))
        risk += 1 + v

def size_fill(p):
    open = [p]
    close = set(open)
    while open:
        for p in ngb(*open.pop()):
            if p not in close and GRID[p[0]][p[1]] < 9:
                close.add(p)
                open.append(p)
    return len(close)

bassins = sorted(map(size_fill, lows), reverse=True)
p2 = reduce(mul, bassins[:3], 1)

print(risk)
print(p2)
