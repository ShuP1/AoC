import sys
from itertools import count

lines = ([tuple(map(int, d.split(','))) for d in l.split('->')]
    for l in sys.stdin.readlines())
MAP = {(x, y) for parts in lines
    for (ax, ay), (bx, by) in zip(parts[:-1], parts[1:])
    for x in range(min(ax, bx), max(ax, bx)+1)
    for y in range(min(ay, by), max(ay, by)+1)}
Y_MAX = max(y for _,y in MAP)

SAND = 500,0
SM = [(0, 1), (-1, 1), (1, 1)]
def sim(ground=float('inf')):
    M = set(MAP)
    for units in count(0):
        if SAND in M:
            break
        x,y = SAND
        while y < Y_MAX+2:
            for dx,dy in SM:
                t = x+dx,y+dy
                if t not in M and t[1] < ground:
                    x,y = t
                    break
            else:
                M.add((x,y))
                break
        else:
            break
    return units

print(sim())
print(sim(Y_MAX+2))
