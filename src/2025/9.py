import sys
from itertools import combinations, pairwise

B = [tuple(map(int, l.strip().split(','))) for l in sys.stdin]

def order(p):
    (ax,ay),(bx,by) = p
    return min(ax,bx), min(ay,by), max(ax,bx), max(ay,by)

p1 = p2 = 0
lines = list(map(order, pairwise(B)))
for ax,ay,bx,by in map(order, combinations(B, 2)):
    area = (bx-ax+1) * (by-ay+1)
    p1 = max(p1, area)
    if area > p2 and not any(
        ax < hx and ay < hy and bx > lx and by > ly
        for lx,ly,hx,hy in lines
    ):
        p2 = area
print(p1)
print(p2)
