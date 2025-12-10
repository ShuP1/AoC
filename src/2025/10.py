import sys
from functools import reduce

B = []
for l in sys.stdin:
    l, *nums = [p[1:-1] for p in l.strip().split()]
    *bss, j = [list(map(int, n.split(','))) for n in nums]
    B.append((l, bss, j))

p1 = 0
for l, bss, _ in B:
    bits = [sum(1<<b for b in bs) for bs in bss]
    r = reduce(lambda l,c: (l<<1)|(c=='#'), reversed(l), 0)
    mask = [-1]*(1<<len(l)); mask[0] = 0
    q = [0]
    for st in q:
        for bs in bits:
            if not ~mask[st^bs]:
                mask[st^bs] = mask[st]+1
                q.append(st^bs)
    p1 += mask[r]
print(p1)

INF = float('inf')
EPS = 1e-9
def simplex(A, C):
    def pivot(r, s):
        k = 1/D[r][s]
        for i in range(m+2):
            if i == r: continue
            for j in range(n+2):
                if j != s: D[i][j] -= D[r][j]*D[i][s]*k
        for i in range(n+2): D[r][i] *= k
        for i in range(m+2): D[i][s] *= -k
        D[r][s] = k; B[r], N[s] = N[s], B[r]
    def find(p):
        while True:
            if D[m+p][s:=min((i for i in range(n+1) if p or N[i] != -1), key=lambda x: (D[m+p][x], N[x]))] > -EPS: return 1
            if (r:=min((i for i in range(m) if D[i][s] > EPS), key=lambda x: (D[x][-1]/D[x][s], B[x]), default=-1)) == -1: return 0
            pivot(r, s)
    m = len(A); n = len(A[0])-1; N = [*range(n), -1]; B = [*range(n, n+m)]; D = [*([*A[i], -1] for i in range(m)), C+[0]*2, [0]*(n+2)]
    for i in range(m): D[i][-2], D[i][-1] = D[i][-1], D[i][-2]
    D[-1][n] = 1; r = min(range(m), key=lambda x: D[x][-1])
    if D[r][-1] < -EPS and (pivot(r, n) or not find(1) or D[-1][-1] < -EPS):
        return -INF, None
    for i in range(m): B[i] == -1 and pivot(i, min(range(n), key=lambda x: (D[i][x], N[x])))
    if find(0):
        x = [0]*n
        for i in range(m):
            if 0 <= B[i] < n: x[B[i]] = D[i][-1]
        return sum(C[i]*x[i] for i in range(n)), x
    else:
        return -INF, None

p2 = 0
for _, bss, j in B:
    u,v = len(j),len(bss)
    g = [[0]*(v+1) for _ in range(2*u+v)]
    for i, bs in enumerate(bss):
        g[-i-1][i] = -1
        for b in bs:
            g[b][i] = 1
            g[b+u][i] = -1
    for i, v in enumerate(j):
        g[i][-1] = v
        g[i+u][-1] = -v
        n = len(g[0])-1

    bval = INF
    bsol = None
    def branch(g):
        global bval, bsol

        val, x = simplex(g, [1]*n)
        if val+EPS >= bval or val == -INF:
            return

        k, v = next(((i, int(e)) for i,e in enumerate(x) if abs(e-round(e))>EPS), (-1, 0))
        if k == -1:
            if val+EPS < bval:
                bval, bsol = val, [*map(round, x)]
        else:
            s = [0]*n+[v]; s[k] = 1
            branch(g+[s])
            s = [0]*n+[~v]; s[k] = -1
            branch(g+[s])
    branch(g)
    p2 += round(bval)
print(p2)
