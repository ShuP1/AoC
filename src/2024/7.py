import sys
from itertools import product
from operator import add, mul

B = [(int(t[:-1]), tuple(map(int, vs)))
    for t,*vs in (l.split() for l in sys.stdin)]

def check(t, vs, ops):
    v0, *vs = vs
    for fs in product(ops, repeat=len(vs)):
        v = v0
        for w,f in zip(vs, fs):
            v = f(v, w)
        if v == t:
            return True
def solve(ops):
    return sum(t for t,vs in B if check(t, vs, ops))
print(solve([add, mul]))

def concat(a, b):
    return a * 10**len(str(b)) + b
print(solve([add, mul, concat]))
