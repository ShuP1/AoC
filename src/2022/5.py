import sys
from copy import deepcopy

lines = sys.stdin.readlines()
limit = next(i for i,l in enumerate(lines) if not l.strip())
g = lines[:limit-1]
g = [[g[x][y] for x in range(limit-2, -1, -1) if g[x][y] != ' ']
    for y in range(1, len(g[0]), 4)]
ins = [(int(n),int(f)-1,int(t)-1) for _,n,_,f,_,t in
    (l.split() for l in lines[limit+1:])]

p1 = deepcopy(g)
for n,f,t in ins:
    for _ in range(n):
        p1[t].append(p1[f].pop())
print(''.join(r[-1] for r in p1))

p2 = deepcopy(g)
for n,f,t in ins:
    l, p2[f] = p2[f][-n:], p2[f][:-n]
    p2[t].extend(l)
print(''.join(r[-1] for r in p2))
