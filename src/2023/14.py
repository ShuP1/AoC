import sys

ls = sys.stdin.readlines()
B = {(x, y): c for y, r in enumerate(ls) for x, c in enumerate(r.strip())}
DOTS = {p for p,c in B.items() if c != '#'}
rs = {p for p,c in B.items() if c == 'O'}

def tilt(rs, d=(0, 1)):
    while True:
        free = DOTS - rs
        nrs = {zd if zd in free else z for z,zd in
            ((z,(z[0]-d[0], z[1]-d[1])) for z in rs)}
        if nrs == rs:
            return nrs
        rs = nrs
def load(rs):
    return round(len(ls)*len(rs) - sum(y for _,y in rs))

print(load(tilt(rs)))

seen = []
while True:
    for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        rs = tilt(rs, d)
    if rs in seen:
        break
    seen.append(rs)
n, m = len(seen), seen.index(rs)
print(load(seen[(1000000000 - n) % (m - n) + n - 1]))
