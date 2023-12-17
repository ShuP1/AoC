import sys
from heapq import heappop, heappush

B = [[int(c) for c in l.strip()] for l in sys.stdin]
Y,X = len(B),len(B[0])

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def solve(n_min, n_max):
    q = [(0, 0, 0, -1)]
    c = set()
    dists = {}
    while q:
        d, y, x, w = heappop(q)
        if y==Y-1 and x==X-1:
            return d
        if (y, x, w) in c:
            continue
        c.add((y, x, w))
        for nw in range(4):
            if nw == w or (nw+2)%4 == w:
                continue
            nd = d
            ny,nx = y,x
            for n in range(n_max):
                ny += D[nw][1]
                nx += D[nw][0]
                if 0<=ny<Y and 0<=nx<X:
                    nd += B[ny][nx]
                    if n+1 >= n_min and nd < dists.get((ny, nx, nw), 1e100):
                        dists[(ny, nx, nw)] = nd
                        heappush(q, (nd, ny, nx, nw))
print(solve(1, 3))
print(solve(4, 10))
