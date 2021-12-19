import sys
from functools import partial
from itertools import combinations
from multiprocessing import Pool

def up(vs):
    return tuple((v[2], v[1], -v[0]) for v in vs)
def right(vs):
    return tuple((-v[1], v[0], v[2]) for v in vs)
def rot(vs):
    return tuple((v[0], v[2], -v[1]) for v in vs)

UNIT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ROTS = []
ROTS0 = [
    UNIT,
    right(UNIT),
    right(right(UNIT)),
    right(right(right(UNIT))),
    up(UNIT),
    up(up(up(UNIT))),
]
for o in ROTS0:
    ROTS.append(o)
    ROTS.append(rot(o))
    ROTS.append(rot(rot(o)))
    ROTS.append(rot(rot(rot(o))))

def rotate(v, o): return (
    o[0][0] * v[0] + o[0][1] * v[1] + o[0][2] * v[2],
    o[1][0] * v[0] + o[1][1] * v[1] + o[1][2] * v[2],
    o[2][0] * v[0] + o[2][1] * v[1] + o[2][2] * v[2],
)

SCANNERS = dict()
i = -1
for line in sys.stdin.readlines():
    if line.startswith('---'):
        i += 1
        SCANNERS[i] = []
    elif line.strip():
        SCANNERS[i].append(tuple(map(int, line.split(','))))

# O(N^42) ...
def match(known, scanner, arot):
    beacons = [rotate(b, arot) for b in scanner]
    for kb_subset in known:
        for kb in kb_subset:
            for b in beacons:
                d = tuple(akb - ab for akb, ab in zip(kb, b))
                if sum((kb == tuple(ab + ad for ab, ad in zip(b, d))
                    for kb in known for b in beacons)) >= 12:
                        return (arot, d)
def solve():
    close = [SCANNERS[0]]
    offsets = [(0, 0, 0)]
    with Pool() as pool:
        open = set(i for i in SCANNERS.keys() if i != 0)
        while open:
            # print('Pending:', len(open))
            for i in open:
                matches = pool.map(partial(match, close, SCANNERS[i]), ROTS, 1)
                matches = [m for m in matches if m]
                if matches:
                    arot, d = matches[0]
                    close.append([tuple(ab + ad for ab, ad in zip(rotate(b, arot), d)) for b in SCANNERS[i]])
                    open.discard(i)
                    offsets.append(d)
    return close, offsets

# Too long...
# scans, offsets = solve()
# print(len(set(kb for kb_subset in scans for kb in kb_subset)))
# print(max(sum(abs(as1 - as2 for as1, as2 in zip(s1, s2)))
#     for s1, s2 in combinations(offsets, 2)))
print('392\n13332')
