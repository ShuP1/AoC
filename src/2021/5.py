import sys
from collections import defaultdict

lines = [[int(v) for p in line.split(' -> ') for v in p.split(',')]
    for line in sys.stdin.readlines()]

def cmp(a, b):
    return 0 if a == b else (-1 if a > b else 1)

ps1 = defaultdict(lambda: 0)
ps2 = defaultdict(lambda: 0)
for x0, y0, x1, y1 in lines:
    hv = x0 == x1 or y0 == y1
    xs = cmp(x0, x1)
    ys = cmp(y0, y1)
    sz = max(abs(x0-x1), abs(y0-y1))+1
    for d in range(sz):
        p = (x0+d*xs, y0+d*ys)
        if hv:
            ps1[p] += 1
        ps2[p] += 1

def score(ps):
    return sum(map(lambda v: v >= 2, ps.values()))

print(score(ps1))
print(score(ps2))
