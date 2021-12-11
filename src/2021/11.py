import sys
from itertools import product, count

GRID = [[*map(int, line.strip())] for line in sys.stdin.readlines()]
N = len(GRID)

def ngb(sx, sy):
    for dx, dy in product(range(-1, 2), repeat=2):
        if dx != 0 or dy != 0:
            x, y = sx+dx, sy+dy
            if 0 <= x < N and 0 <= y < N:
                yield (x, y)

def step():
    flash = set()
    queue = []
    def inc(p):
        x, y = p
        GRID[x][y] += 1
        if GRID[x][y] > 9 and p not in flash:
            flash.add(p)
            queue.append(p)

    for p in product(range(N), repeat=2):
        inc(p)

    while queue:
        for p in ngb(*queue.pop()):
            inc(p)

    for x, y in flash:
        GRID[x][y] = 0

    return len(flash)

STEPS1 = 100
print(sum(step() for _ in range(STEPS1)))
print(next(n for n in count(STEPS1+1) if step() >= N*N))
