import sys

I = [l.strip() for l in sys.stdin]
Y,X = len(I),len(I[0])

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def solve(y, x, d):
    q = [(y, x, d)]
    seen = set(q)
    def enqueue(y, x, d):
        p = (y+D[d][0], x+D[d][1], d)
        if 0 <= p[0] < Y and  0 <= p[1] < X and p not in seen:
            seen.add(p)
            q.append(p)
    while q:
        y,x,d = q.pop()
        c = I[y][x]
        if c == '/':
            enqueue(y,x,3-d)
        elif c == '\\':
            enqueue(y,x,{0:1, 1:0, 2:3, 3:2}[d])
        elif c in '|-' and (c == '-') == d%2:
            enqueue(y,x,(d-1)%4)
            enqueue(y,x,(d+1)%4)
        else:
            enqueue(y,x,d)
    return len({(x,y) for x,y,_ in seen})

print(solve(0,0,0))
print(max(
    max(solve(y, 0, 0) for y in range(Y)),
    max(solve(y, X-1, 2) for y in range(Y)),
    max(solve(0, x, 1) for x in range(X)),
    max(solve(Y-1, x, 3) for x in range(X))
))
