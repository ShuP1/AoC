import sys

R, A = [m.splitlines() for m in sys.stdin.read().split('\n\n')]
R = [tuple(map(int, r.split('-'))) for r in R]
A = [int(a) for a in A]

print(sum(any(l <= a <= h for l, h in R) for a in A))

p2 = 0
i = 0
for a,b in sorted(R):
    if a <= i:
        if i < b:
            p2 += b - i
            i = b
    else:
        p2 += b - a + 1
        i = b
print(p2)
