import sys
from itertools import count

V = int(sys.stdin.readline())

def p1():
    n = 1
    while n * n < V:
        n += 2
    d = n * n - V
    while d >= n:
        d -= n
    h = n // 2
    return abs(d-h) + h

def p2():
    grid = {(0, 0): 1}
    for n in count(1):
        p = n, -n
        for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            for _ in range(2*n):
                p = p[0]+dx, p[1]+dy
                v = sum(grid.get((p[0]+nx, p[1]+ny), 0) for nx, ny in
                    [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)])
                if v > V:
                    return v
                grid[p] = v

print(p1())
print(p2())
