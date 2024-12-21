import sys
from functools import cache

B = [l.strip() for l in sys.stdin]

def path(s):
    ps = {c: (x,y)
        for y,l in enumerate(s.splitlines())
        for x,c in enumerate(l)}
    xs,ys = ps[' ']
    @cache
    def inner(start, end):
        x1,y1 = ps[start]
        x2,y2 = ps[end]
        dx,dy = x2-x1, y2-y1
        vx = ("<"*-dx) + (">"*dx)
        vy = ("^"*-dy) + ("v"*dy)

        ko = xs-x1, ys-y1
        if (dx>0 or ko==(dx,0)) and ko!=(0,dy):
            vx,vy = vy,vx
        return vx+vy+'A'
    return inner

Nf = path("789\n456\n123\n 0A")
Df = path(" ^A\n<v>")

def solve(l, d, Xf=Nf):
    return sum(rec(Xf(p, c), d)
        for c, p in zip(l, 'A' + l[:-1]))
@cache
def rec(l, d):
    if d == 0:
        return len(l)
    return solve(l, d-1, Df)

print(sum(int(l[:-1]) * solve(l, 2) for l in B))
print(sum(int(l[:-1]) * solve(l, 25) for l in B))
