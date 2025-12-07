import sys
from collections import Counter

B = [l.strip() for l in sys.stdin]
S = B[0].index('S')

beams = {S}
p1 = 0
for l in B:
    nxt = set()
    for i in beams:
        if l[i] == '^':
            p1 += 1
            nxt.add(i-1)
            nxt.add(i+1)
        else:
            nxt.add(i)
    beams = nxt
print(p1)

beams = Counter([S])
for l in B:
    nxt = Counter()
    for i, n in beams.items():
        if l[i] == '^':
            nxt[i-1] += n
            nxt[i+1] += n
        else:
            nxt[i] += n
    beams = nxt
print(sum(beams.values()))

