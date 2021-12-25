import sys
from collections import defaultdict
from itertools import accumulate, product
from functools import reduce

lines = (line.strip().split(' => ') for line in sys.stdin.readlines())
def tup(l): return tuple(map(tuple, l.split('/')))
MAP = {tup(t): tup(f) for t,f in lines}

P = tup('.#./..#/###')

def rotate(p, i):
    return tuple(zip(*reversed(p)))
def sames(p):
    yield from accumulate(range(3), rotate, initial=p)
    yield from accumulate(range(3), rotate, initial=p[::-1])

def step(old, i):
    D = 2 if len(old)%2==0 else 3
    S = len(old)//D*(D+1)
    new = [['']*S for _ in range(S)]
    for X, Y in product(range(len(old)//D), repeat=2):
        p = tuple(tuple(r[X*D:(X+1)*D]) for r in old[Y*D:(Y+1)*D])
        q = next(MAP[q] for q in sames(p) if q in MAP)
        for x, y in product(range(D+1), repeat=2):
            new[Y*(D+1)+y][X*(D+1)+x] = q[y][x]
    return new

def solve(n):
    p = reduce(step, range(n), P)
    return sum(r.count('#') for r in p)

print(solve(5))
print(solve(18))
