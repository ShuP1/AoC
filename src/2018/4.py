import sys
from collections import defaultdict

lines = sorted(sys.stdin.readlines())

at, cur = 0, 0
guards = defaultdict(lambda: [0] * 60)
for line in lines:
    parts = line.split()
    k = parts[2]
    m = int(parts[1][-3:-1])
    if k == 'Guard':
        cur = int(parts[3][1:])
        h = int(parts[1][-6:-4])
        at = 0 if h > 0 else m
    elif k == 'falls':
        at = m
    elif k == 'wakes':
        for n in range(at, m):
            guards[cur][n] += 1

g1 = max(guards, key=lambda g: sum(guards[g]))
print(g1 * max(range(60), key=lambda i: guards[g1][i]))

p2 = max(((g, *max(enumerate(ts), key=lambda t: t[1]))
    for g, ts in guards.items()), key=lambda t: t[2])
print(p2[0] * p2[1])
