import sys
from collections import deque
from itertools import combinations

G = {l[1]: (int(l[4][5:-1]), set(v.strip(',') for v in l[9:]))
    for l in (l.strip().split() for l in sys.stdin.readlines())}
F = {k for k,(f, _) in G.items() if f}
S, T = 'AA', 30

def path(f, g) -> int:
    q = deque([(f, 0)])
    c = set()
    while q:
        p, d = q.popleft()
        if p not in c:
            c.add(p)
            d += 1
            for t in G[p][1]:
                if t == g:
                    return d
                q.append((t, d))
GF = {f: {t: path(f, t) for t in F if t!=f} for f in F}

def solve_one(v, subset, sec, sco, best):
    sec -= 1
    if sec <= 0:
        return sco
    sco += G[v][0]*sec
    best = max(best, sco)
    subset = subset-set([v])

    isco = sco
    for nv, d in GF[v].items():
        nsec = sec-d
        if nsec > 0 and nv in subset:
            sco = max(sco, solve_one(nv, subset, nsec, isco, best))
    return sco

def solve(subset=F, sec=T):
    return max((solve_one(f, subset, sec-path(S, f), 0, 0)
        for f in subset), default=0)

print(solve())
print(max(
    solve(set(elephant), T-4)+solve(F.difference(elephant), T-4)
    for n in range(len(F)+1) for elephant in combinations(F, n)))
