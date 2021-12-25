import sys
from collections import Counter

LIST = dict()
for line in sys.stdin.readlines():
    kv = line.strip().split(' -> ')
    a, c = kv[0].split()
    LIST[a] = (int(c[1:-1]), kv[1].split(', ') if len(kv) > 1 else [])

bottom = next(p for p in LIST if all(map(lambda cd: p not in cd[1], LIST.values()))) 
print(bottom)

def balance(p):
    c, ds = LIST[p]
    if not ds:
        return c
    subs = list(map(balance, ds))
    if any(s != subs[0] for s in subs):
        i = next(i for i in range(len(subs))
            if all(s != subs[i] or j == i for j, s in enumerate(subs)))
        need = subs[(i+1)%len(subs)]
        print(LIST[ds[i]][0]+need-subs[i])
        subs[i] = need
    return c + sum(subs)
balance(bottom)
