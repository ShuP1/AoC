import sys

B, M = sys.stdin.read().split('\n\n')
B = [l.strip() for l in B.split('\n')]
M = M.replace('\n', '')

DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

G = {}
for y, l in enumerate(B):
    for x, c in enumerate(l):
        G.setdefault(c, set()).add((y, x))
S = G['@'].pop()
WALLS = G['#']
boxes = set(G['O'])

def va(u,v):
    return u[0]+v[0], u[1]+v[1]

p = S
for d in map(DIRS.get, M):
    qp = va(p, d)
    n = 1
    while qp in boxes:
        qp = va(qp, d)
        n += 1
    if qp not in WALLS:
        p = va(p, d)
        if n > 1:
            boxes.remove(p)
            boxes.add(qp)
print(sum(100*y+x for y,x in boxes))


WALLS = set()
for y, x in G['#']:
    x *= 2
    WALLS.add((y, x))
    WALLS.add((y, x + 1))

boxes = {}
for y, x in G['O']:
    x *= 2
    p = (y, x), (y, x + 1)
    boxes[p[0]] = p
    boxes[p[1]] = p

p = S[0], S[1] * 2
for d in map(DIRS.get, M):
    np = va(p, d)
    q = [np]
    moves = set()
    while q:
        qp = q.pop()
        if qp in WALLS:
            break
        if qp not in boxes:
            continue
        box = boxes[qp]
        if box in moves:
            continue
        moves.add(box)
        a,b = box
        if d != DIRS['<']:
            q.append(va(b, d))
        if d != DIRS['>']:
            q.append(va(a, d))
    else:
        p = np
        for a, b in moves:
            del boxes[a]
            del boxes[b]
        for a, b in moves:
            na, nb = va(a, d), va(b, d)
            boxes[na] = (na, nb)
            boxes[nb] = (na, nb)

print(sum(100*y+x for (y,x),_ in boxes.values()) // 2)
