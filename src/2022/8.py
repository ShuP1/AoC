import sys
from itertools import product
from math import prod

G = [[int(t) for t in l.strip()] for l in sys.stdin.readlines()]
DIR = [(-1,0),(0,1),(1,0),(0,-1)]
Y, X = len(G), len(G[0])

def view(x, y, dx, dy):
    t = G[y][x]
    x += dx
    y += dy
    n = 0
    while 0<=y<Y and 0<=x<X:
        n += 1
        if G[y][x] >= t:
            return False, n
        x += dx
        y += dy
    return True, n

print(sum(any(view(*p, *d)[0] for d in DIR)
    for p in product(range(X), range(Y))))

print(max(prod(view(*p, *d)[1] for d in DIR)
    for p in product(range(X), range(Y))))
