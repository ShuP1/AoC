import sys
from collections import deque

M = [list(l.strip()) for l in sys.stdin.readlines()]
Y, X = len(M), len(M[0])

find=lambda v: ((x,y) for y,row in enumerate(M) for x,c in enumerate(row) if c == v)
S, E = next(find('S')), next(find('E'))
M[S[1]][S[0]] = 'a'
M[E[1]][E[0]] = 'z'

def path_len(starts):
    starts = list(starts)
    q = deque([(s, 0) for s in starts])
    c = set(starts)
    while q:
        (x, y), n = q.popleft()
        h = ord(M[y][x])+1
        n += 1
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            tx, ty = x+dx,y+dy
            if 0<=tx<X and 0<=ty<Y and ord(M[ty][tx]) <= h:
                t = tx,ty
                if t == E:
                    return n
                if t not in c:
                    c.add(t)
                    q.append((t, n))
    return float('inf')
print(path_len([S]))
print(path_len(find('a')))
