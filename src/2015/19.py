import sys
from itertools import count
from collections import defaultdict

lines = sys.stdin.readlines()
target = lines.pop(-1).strip()
lines.pop(-1)

rep = defaultdict(list)
rev = defaultdict(list)
for line in lines:
    f, t = line.strip().split(' => ')
    rep[f].append(t)
    rev[t].append(f)

dis = set()
def apply(tr, new, old, rep):
    for f, ts in rep.items():
        l = len(f)
        i = 0
        while True:
            p = tr.find(f, i)
            if p < 0:
                break
            for t in ts:
                s = tr[:p] + t + tr[p+l:]
                if not (s in old):
                    new.add(s)
            i = p+1
    return new

print(len(apply(target, set(), set(), rep)))


# Exploding
"""
prev = set([target])
old = set().union(prev)
for n in count(1):
    new = set()
    for t in prev:
        apply(t, new, old, rev)
    
    if 'e' in new:
        print(n)
        break
    prev = new
    old = old.union(prev)
"""

# Cheat code
mls = sum(map(lambda s: s.isupper(), target))
print(mls - (target.count("Rn") + target.count("Ar") + 2*target.count("Y") + 1))
