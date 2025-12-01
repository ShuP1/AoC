import sys

B = [(1 if l[0] == 'R' else -1, int(l[1:].strip())) for l in sys.stdin]

r = 50
p1, p2 = 0, 0
for s, v in B:
    for _ in range(v):
        r += s
        r %= 100
        if r == 0:
            p2 += 1
    if r == 0:
        p1 += 1
print(p1)
print(p2)
