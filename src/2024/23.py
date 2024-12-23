import sys
from collections import deque

B = [l.strip().split('-') for l in sys.stdin]
G = {}
for a,b in B:
    G.setdefault(a, set()).add(b)
    G.setdefault(b, set()).add(a)

def cliques():
    idx = {}
    nb = {}
    for k,ts in G.items():
        idx[k] = len(idx)
        nb[k] = {v for v in ts if v not in idx}

    q = deque(([k], sorted(nb[k], key=idx.get)) for k in G)
    while q:
        v, cnb = map(list, q.popleft())
        yield v
        for i, k in enumerate(cnb):
            q.append((v + [k], [v for v in cnb[i + 1:] if v in nb[k]]))

print(sum(len(vs) == 3 and any(v[0] == 't' for v in vs)
    for vs in cliques()))
print(','.join(sorted(max(cliques(), key=len))))
