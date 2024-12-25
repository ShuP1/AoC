import sys
from itertools import product

L, K = [], []
for b in sys.stdin.read().split('\n\n'):
    v = tuple(r.count('#') for r in zip(*b.splitlines()))
    [K, L][b[0][0] == '#'].append(v)

Y = len(L[0])+2
print(sum(all(u+v <= Y for u,v in zip(l,k))
    for l,k in product(L, K)))
