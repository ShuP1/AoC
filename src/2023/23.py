import sys

B = [l.strip() for l in sys.stdin]
Y,X = len(B), len(B[0])

S = 0,B[0].index('.')
def solve(adjs):
    mx = 0
    q = [(S, 0)]
    cs = set()
    while q:
        f,d = q.pop()
        if d == -1:
            cs.remove(f)
            continue
        if f[0] == Y-1:
            mx = max(mx, d)
            continue
        if f in cs:
            continue
        cs.add(f)
        q.append((f, -1))
        for t,l in adjs(f):
            q.append((t, d+l))
    return mx

D = [(1,0), (0,1), (-1,0), (0,-1)]
DS = {
    '.': D,
    '>': [(0,1)],
    'v': [(1,0)],
}

def p1(f):
    y,x = f
    for dy,dx in DS[B[y][x]]:
        t = ny,nx = y+dy,x+dx
        if 0<=ny<Y and 0<=nx<X and B[ny][nx] != '#':
            yield t,1
print(solve(p1))

E = {}
for y, r in enumerate(B):
    for x, c in enumerate(r):
        if c != '#':
            f = y,x
            for dy,dx in D:
                t = ny,nx = y+dy, x+dx
                if 0<=ny<Y and 0<=nx<X and B[ny][nx] != '#':
                    E.setdefault(f, set()).add((t, 1))
                    E.setdefault(t, set()).add((f, 1))
while True:
    t = next(filter(lambda t: len(t[1]) == 2, E.items()), None)
    if not t:
        break
    p, ((ta, da), (tb, db)) = t
    E[ta].remove((p, da))
    E[tb].remove((p, db))
    E[ta].add((tb, da+db))
    E[tb].add((ta, da+db))
    E.pop(p)
print(solve(lambda f: E[f]))
