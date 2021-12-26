import sys
from itertools import product
from collections import defaultdict

lines = (line.split() for line in sys.stdin.readlines())
CLAIMS = [(*map(int, l[2][:-1].split(',') + l[3].split('x')),) for l in lines]

inches = defaultdict(int)
for x, y, nx, ny in CLAIMS:
    for p in product(range(x, x+nx), range(y, y+ny)):
        inches[p] += 1
print(sum(n>1 for n in inches.values()))

def overlap(a, b):
    ax, ay, anx, any = a
    bx, by, bnx, bny = b
    return ax < bx+bnx and ax+anx > bx \
        and ay < by+bny and ay+any > by
print(next(i for i, a in enumerate(CLAIMS, 1) if
    not any(a!=b and overlap(a, b) for b in CLAIMS)))