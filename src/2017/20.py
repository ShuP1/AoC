import sys
from collections import defaultdict
from math import sqrt

PVA = [tuple(tuple(map(int, p[3:-1].split(',')))
    for p in line.strip().split(', '))
    for line in sys.stdin.readlines()]

def dist(p): return sum(map(abs, p))

def p_at(pva, t):
    p,v,a = pva
    dt = t*(t+1)/2
    return tuple(p[i] + v[i]*t + (a[i]*dt) for i in range(len(p)))

print(min( (dist(p_at(pva, 10_000)), i)
    for i, pva in enumerate(PVA))[1])

def roots(a, b, c):
    if a == 0:
        return [-c / b] if b != 0 else []
    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    return [x1, x2] if x1 != x2 else [x1]

def collision(a, b):
    u = (a[2][0] - b[2][0]) / 2
    x_equals = roots(u, a[1][0] - b[1][0] + u, a[0][0] - b[0][0])
    return min((t for t in x_equals if t >= 0 and
        all(abs(va - vb) < .01 for va, vb in zip(p_at(a, t), p_at(b, t)))), default=None)

collisions = defaultdict(set)
for i in range(len(PVA)):
    for j in range(i+1, len(PVA)):
        t = collision(PVA[i], PVA[j])
        if t is not None:
            collisions[t].add(i)
            collisions[t].add(j)

remaining = set(range(len(PVA)))
for t in sorted(collisions.keys()):
    ps = collisions[t]
    if len(remaining.intersection(ps)) > 1:
        for p in ps:
            remaining.remove(p)
print(len(remaining))
