import sys
from functools import cache
from re import match

I = [((p := l.split())[0], tuple(map(int, p[1].split(','))))
     for l in sys.stdin.readlines()]

@cache
def solve(s, vs):
    if not s:
        return int(not vs)
    v = 0
    if s[0] != '#':
        v = solve(s[1:], vs)
    if vs and match(r'[#?]{%d}[.?]'%vs[0], s):
        return v + solve(s[vs[0]+1:], vs[1:])
    return v

print(sum(solve(s + '.', vs) for s, vs in I))
print(sum(solve('?'.join([s] * 5) +'.', vs * 5) for s, vs in I))
