import sys, random
from math import prod
from collections import deque, defaultdict

B = {(p := l.strip().split())[0][:-1]: set(p[1:]) for l in sys.stdin}
for k,vs in list(B.items()):
    for v in vs:
        B.setdefault(v, set()).add(k)

def paths(frm, skips=set()):
    pred = {frm: frm}
    q = deque([frm])
    while q:
        n = q.popleft()
        for to in B[n]:
            if to in pred or (n, to) in skips or (to, n) in skips:
                continue
            pred[to] = n
            q.append(to)
    return pred

uses = defaultdict(lambda: 0)
for _ in range(len(B)):
    a,n = random.sample(list(B.keys()), 2)
    pred = paths(a)
    m = pred[n]
    while m != a:
        uses[tuple(sorted([n,m]))] += 1
        n,m = pred[m],n

banned = sorted(uses.keys(), key=lambda x: uses[x])[-3:]
ns = [len(paths(u, banned)) for u in banned[0]]
assert ns[0] != ns[1]
print(prod(ns))
