import sys
from collections import defaultdict, deque

M = {(x,y) for y,row in enumerate(sys.stdin.readlines())
    for x,c in enumerate(row.strip()) if c == '#'}

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def solve(limit=2**32):
    dirs = deque([
        ((-1, -1), (0, -1), (1, -1)),
        ((-1, 1), (0, 1), (1, 1)),
        ((-1, 1), (-1, 0), (-1, -1)),
        ((1, 1), (1, 0), (1, -1))
    ])
    m = M
    for n in range(1, limit+1):
        goals = defaultdict(list)
        for p in m:
            if all(add(p, d) not in m for ds in dirs for d in ds):
                continue
            for ds in dirs:
                if all(add(p, d) not in m for d in ds):
                    goals[add(p, ds[1])].append(p)
                    break
        moved = {k: v[0] for k,v in goals.items() if len(v) == 1}
        if not moved:
            return n
        m = (m - set(moved.values())) | moved.keys()
        dirs.rotate(-1)
    return (max(x for x,_ in m) - min(x for x,_ in m) + 1) * (max(y for _,y in m) - min(y for _,y in m) + 1) - len(m)

print(solve(10))
print(solve())
