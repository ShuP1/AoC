import sys
from functools import cache
from itertools import combinations
from random import randint

R, O = sys.stdin.read().split('\n\n')
R = {c: int(v) for c, v in (l.split(': ') for l in R.splitlines())}
O = {t: (u,v,o) for u,o,v,_,t in map(str.split, O.splitlines())}

ZS = sorted((k for k in O if k[0] == 'z'), reverse=True)
def solve(rs=R, swaps={}):
    @cache
    def rec(k):
        if k in rs:
            return rs[k]
        if k in swaps:
            k = swaps[k]
        u, v, o = O[k]
        u = rec(u)
        v = rec(v)
        match o:
            case 'AND': return u & v
            case 'OR' : return u | v
            case 'XOR': return u ^ v
    try:
        return int(''.join(map(str, map(rec, ZS))), 2)
    except RecursionError:
        return 0

print(solve())

N = len(R) // 2
N_max = (1 << N)

def check(swaps, bit):
    mask = (1 << bit) - 1
    rs = {}
    for _ in range(99):
        x = randint(0, N_max)
        y = randint(0, N_max)
        z = (x + y) & mask
        for i in range(N):
            rs[f'x{i:02}'] = x & 1
            x >>= 1
            rs[f'y{i:02}'] = y & 1
            y >>= 1
        if solve(rs, swaps) & mask != z:
            return False
    return True

swaps = {}
for bit in range(N+1):
    if check(swaps, bit):
        continue
    for u, v in combinations(O.keys(), 2):
        ns = swaps.copy()
        ns[u] = v
        ns[v] = u
        if check(ns, bit):
            swaps = ns
            break
print(','.join(sorted(swaps.values())))
