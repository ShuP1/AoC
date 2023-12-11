import sys
from itertools import combinations

M = sys.stdin.readlines()
G = {(x, y) for y, r in enumerate(M) for x, c in enumerate(r) if c == '#'}

EX, EY = set(x for x, _ in G), set(y for _, y in G)
def solve(e=1):
    GE = {(x+sum(ex not in EX for ex in range(x))*e, y+sum(ey not in EY for ey in range(y))*e) for x, y in G}
    return sum(abs(xb-xa)+abs(yb-ya) for (xa, ya), (xb, yb) in combinations(GE, 2))

print(solve())
print(solve(1000000-1))
