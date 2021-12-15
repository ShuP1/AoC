import sys
from heapq import heappop, heappush

GRID = [[*map(int, line.strip())] for line in sys.stdin.readlines()]

def path(grid):
    e = len(grid)-1
    end = (e, e)
    close = dict()
    heap = [(0, (0, 0))]
    while heap:
        cost, at = heappop(heap)
        if at in close and cost >= close[at]:
            continue
        close[at] = cost

        if at == end:
            return cost

        sx, sy = at
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x, y = sx+dx, sy+dy
            if 0 <= x <= e and 0 <= y <= e:
                heappush(heap, (cost + grid[y][x], (x, y)))

print(path(GRID))
print(path([[(v + dx + dy - 1) % 9 + 1
    for dx in range(5) for v in row]
    for dy in range(5) for row in GRID
]))
