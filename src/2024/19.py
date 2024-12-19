import sys
from functools import cache

P, L = sys.stdin.read().split('\n\n')
P = P.strip().split(', ')
L = list(map(str.strip, L.splitlines()))

@cache
def count(l):
    if l == '':
        return 1
    return sum(count(l[len(p):]) for p in P
               if l.startswith(p))

print(sum(count(l) > 0 for l in L))
print(sum(map(count, L)))
