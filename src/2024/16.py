import sys

B = [l.strip() for l in sys.stdin]

def find(v):
    return next((x, y) for y, l in enumerate(B)
                for x, c in enumerate(l) if c == v)
S, E = find('S'), find('E')

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
INF = float("inf")

best, paths = INF, set()
q, seen = [((S,), 0, 0)], {(S, 0): 0}
while q:
    path, d, c = q.pop()
    if best < c:
        continue
    p = path[-1]
    if p == E:
        if c < best:
            best, paths = c, set(path)
        else:
            paths.update(path)
        continue
    x, y = p
    dx, dy = DIRS[d]
    if c < best:
        np = nx, ny = x + dx, y + dy
        if B[ny][nx] != "#":
            pd = np, d
            if c < seen.get(pd, INF):
                q.append((path + (np,), d, c+1))
                seen[pd] = c+1
    nc = c + 1000
    if nc < best:
        for nd in (d - 1) % 4, (d + 1) % 4:
            pd = p, nd
            if nc <= seen.get(pd, INF):
                q.append((path, nd, nc))
                seen[pd] = nc
print(best)
print(len(paths))
