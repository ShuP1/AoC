import sys
from itertools import count

grid = [list(row.strip()) for row in sys.stdin.readlines()]

def step():
    moves = False
    for C, (DX, DY) in [('>', (1, 0)), ('v', (0, 1))]:
        tries = ( ((x, y), ((x+DX)%len(row), (y+DY)%len(grid)))
            for y, row in enumerate(grid) for x, c in enumerate(row) if c == C )
        movables = { f: t for f, t in tries if grid[t[1]][t[0]] == '.' }
        if movables:
            moves = True
        for (fx, fy), (tx, ty) in movables.items():
            grid[fy][fx] = '.'
            grid[ty][tx] = C
    return moves

for n in count(1):
    if not step():
        break
print(n)
