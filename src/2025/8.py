import sys
from itertools import combinations

B = [tuple(map(int, l.strip().split(','))) for l in sys.stdin]
N = 1000 if len(B) > 20 else 10

nets = [{p} for p in B]
def connect(a, b):
    net_a = next(n for n in nets if a in n)
    if b not in net_a:
        inet_b = next(i for i, n in enumerate(nets) if b in n)
        net_a |= nets.pop(inet_b)

def dist_t(t):
    (ax, ay, az), (bx, by, bz) = t
    return (ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2

pairs = sorted(combinations(B, 2), key=dist_t)

for a, b in pairs[:N]:
    connect(a, b)
u,v,w,*_ = sorted(map(len, nets), reverse=True)
print(u * v * w)

for a, b in pairs[N:]:
    connect(a, b)
    if len(nets) <= 1:
        break
print(a[0] * b[0])
