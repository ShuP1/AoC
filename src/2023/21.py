import sys

B = [l.strip() for l in sys.stdin]
L = len(B)
assert L == len(B[0])

PS = {x+y*1j for y,r in enumerate(B) for x,c in enumerate(r) if c=='.'}
S,=(x+y*1j for y,r in enumerate(B) for x,c in enumerate(r) if c=='S')
PS.add(S)

D = -1j,1,-1,1j
q = {S}
for _ in range(64):
    q = {p+d for p in q for d in D if p+d in PS}
print(len(q))

N = 26501365
# 26501365%131 == 65

OPEN_PS = {S}
for _ in range(L):
    OPEN_PS = {p+d for p in OPEN_PS for d in D+(0,) if p+d in PS}

even_ps = q
q = {S}
for _ in range(65):
    q = {p+d for p in q for d in D if p+d in PS}
odd_ps = q

out_odd_ps = {x+y*1j for x in range(L) for y in range(not x%2,L,2)} & OPEN_PS - odd_ps
out_even_ps = {x+y*1j for x in range(L) for y in range(x%2,L,2)} & OPEN_PS - even_ps
out_ps = {c for c in out_odd_ps if (c.real-65)*(c.imag-65)>0} | {c for c in out_even_ps if (c.real-65)*(c.imag-65)<0
}.union({c for c in out_odd_ps if (c.real-65)*(c.imag-65)<0} | {c for c in out_even_ps if (c.real-65)*(c.imag-65)>0})

L2 = (2*N+1)//L//2
print((L2+1)**2 * len(odd_ps) + L2 * (L2+1) * len(out_ps)
      + L2**2 * len(even_ps))
