import sys

def dist(sx, sy, bx, by):
    return abs(sx-bx)+abs(sy-by)

sensors = (l.split(' ') for l in sys.stdin.readlines())
sensors = [tuple(int(v[2:-1]) for v in (sx,sy,bx,by))
    for _,_,sx,sy,_,_,_,_,bx,by in sensors]
beacons = {(x, y) for _,_,x,y in sensors}
sensors = [(t[0], t[1], dist(*t)) for t in sensors]

def no_beacon(y=2000000):
    cannot = set()
    for sx, sy, d in sensors:
        off = abs(sy-y)
        for x in range(sx-d+off, sx+d+1-off):
            cannot.add(x)
    bs = {bx for bx,by in beacons if by==y}
    return len(cannot-bs)
print(no_beacon())

L,H = 0,4000000
def distress():
    for sx, sy, d in sensors:
        for i in range(d):
            for x, y in [
                (sx + i, sy + d - 1 - i),
                (sx - i, sy + d - 1 - i),
                (sx + i, sy - d - 1 + i),
                (sx - i, sy - d - 1 + i)
            ]:
                if L <= x <= H and L <= y <= H and (x, y) not in beacons:
                    for s2x, s2y, d2 in sensors:
                        if dist(s2x, s2y, x, y) <= d2:
                            break
                    else:
                        return x * 4000000 + y
print(distress())
