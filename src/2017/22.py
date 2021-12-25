import sys

lines = sys.stdin.readlines()
GRID = {(x, y) for y, row in enumerate(lines)
    for x, c in enumerate(row) if c == '#'}
DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solve(N, W=0, F=0):
    grid = {p: W+1 for p in GRID}
    x, y, d = max(x for x, _ in GRID)//2, max(y for _, y in GRID)//2, 3
    infect = 0
    for _ in range(N):
        p = (x, y)
        s = grid.get(p, 0)
        if s == 0:
            d -= 1
        if s == W:
            infect += 1
        if s == W+1:
            d += 1
        elif s == W+F+1:
            d += 2
        d %= 4
        if s == W+F+1:
            del grid[p]
        else:
            grid[p] = s+1
        dx, dy = DS[d]
        x += dx
        y += dy
    return infect

print(solve(10000))
print(solve(10000000, 1, 1))
