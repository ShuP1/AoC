import sys
from itertools import permutations

B = [l.strip() for l in sys.stdin]
Y, X = len(B), len(B[0])

A = {}
for y, l in enumerate(B):
    for x, c in enumerate(l):
        if c != '.':
            A.setdefault(c, []).append((x, y))

nodes = set()
for ps in A.values():
    for (y1, x1),(y2, x2) in permutations(ps, 2):
        y, x = y1*2 - y2, x1*2 - x2
        if 0 <= y < Y and 0 <= x < X:
            nodes.add((y, x))
print(len(nodes))

for ps in A.values():
    for (y, x),(y2, x2) in permutations(ps, 2):
        dy, dx = y2 - y, x2 - x
        while 0 <= y < Y and 0 <= x < X:
            nodes.add((y, x))
            y += dy
            x += dx
print(len(nodes))
