import sys
from itertools import product
from collections import deque

GRID = dict() # (x, y): (used, size)
for line in sys.stdin.readlines()[2:]:
    parts = line.split()
    node = parts[0].split('-')
    GRID[(int(node[1][1:]), int(node[2][1:]))] = (int(parts[2][:-1]), int(parts[1][:-1]))

pairs = sum(a != b and GRID[a][0] > 0 and GRID[a][0] < (GRID[b][1] - GRID[b][0])
    for a, b in product(GRID, repeat=2))
print(pairs)

def path():
    MOVER_P, MOVER_S = next((p, s[1]) for p, s in GRID.items() if s[0] == 0)
    DATA_P = (max(x for x,_ in GRID), 0)
    WALLS = {p for p, s in GRID.items() if s[0] > MOVER_S}

    close = set([MOVER_P])
    queue = deque([(MOVER_P, 0)])
    while queue:
        p, n = queue.popleft()
        if p == DATA_P:
            return n + (DATA_P[0] - 1) * 5

        x, y = p
        n += 1
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            p = x+dx, y+dy
            if p in GRID and p not in WALLS and p not in close:
                close.add(p)
                queue.append((p, n))

print(path())
