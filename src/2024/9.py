import sys

B = sys.stdin.readline().strip()

M = []
for p, n in enumerate(map(int, B)):
    p = p // 2 if p % 2 == 0 else -1
    M.extend([p] * n)
while -1 in M:
    M[M.index(-1)] = M.pop()
print(sum(i*j for i,j in enumerate(M)))


files, holes = [], []
p = 0
for n, k in enumerate(map(int, B)):
    if k:
        if n % 2 == 0:
            files.append((n // 2, p, k))
        else:
            holes.append((p, k))
    p += k
files.reverse()

res = 0
for j, fp, fsz in files:
    hi = next((i for i, (hp, hsz) in enumerate(holes)
               if hp < fp and hsz >= fsz), None)
    if hi is not None:
        fp, hsz = holes[hi]
        if hsz > fsz:
            holes[hi] = (fp + fsz, hsz - fsz)
        else:
            holes.pop(hi)
    res += sum(range(fp, fp + fsz))*j
print(res)
