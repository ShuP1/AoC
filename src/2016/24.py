import sys
from collections import deque

MAP = sys.stdin.readlines()
NUMS = {int(c): (x, y) for y, row in enumerate(MAP) for x, c in enumerate(row) if c.isnumeric()}
START = NUMS.pop(0)

def solve():
    rem = set(NUMS.values())
    close = set([(START, tuple(rem))])
    queue = deque([(START, rem, 0)])
    p1 = None
    while queue:
        p, rem, n = queue.popleft()
        if not rem:
            if not p1:
                p1 = n
            if p == START:
                return p1, n

        x, y = p
        n += 1
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            p = x+dx, y+dy
            if MAP[p[1]][p[0]] != '#':
                r = rem - {p}
                k = (p, tuple(r))
                if k not in close:
                    close.add(k)
                    queue.append((p, r, n))

print(*solve(), sep='\n')
