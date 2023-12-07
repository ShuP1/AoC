import sys
from collections import Counter

H = [line.split() for line in sys.stdin.readlines()]

C = 'J23456789TXQKA'
KS = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)]
def score(h, j=''):
    if not j: h = h.replace('J', 'X')
    kind = KS.index(tuple(sorted(Counter(h.replace('J', j)).values())))
    return kind, *[C.index(i) for i in h]

def win(fn):
    hs = sorted(H, key=lambda t: fn(t[0]))
    return sum(i*int(b) for i,(_,b) in enumerate(hs, 1))
print(win(score))
print(win(lambda h: max(score(h, i) for i in C[1:])))
