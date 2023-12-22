import sys
from collections import defaultdict

B = [tuple(map(int, l.replace('~', ',').split(','))) for l in sys.stdin]
B.sort(key=lambda b: b[2])

def drop(bs):
    falls = 0
    fallen = []
    high = defaultdict(int)
    for lx,ly,lz, hx,hy,hz in bs:
        top = max(high[(x, y)] for x in range(lx, hx+1) for y in range(ly, hy+1))
        dz = max(0, lz - top - 1)
        falls += bool(dz)
        fallen.append((lx, ly, lz - dz, hx, hy, hz - dz))
        for x in range(lx, hx+1):
            for y in range(ly, hy+1):
                high[(x, y)] = hz - dz
    return falls, fallen

_,fallen = drop(B)
falls = [drop(fallen[:i] + fallen[i+1:])[0] for i in range(len(fallen))]

print(sum(not f for f in falls))
print(sum(falls))
