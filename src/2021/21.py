import sys
from itertools import cycle, islice, product
from collections import Counter, deque

PS = [int(line.split()[4])-1 for line in sys.stdin.readlines()]
N=10

def run():
    ps = [*PS]
    ss = [0, 0]
    dice = cycle(range(1, 100+1))
    rolls = 0
    while True:
        for p in range(2):
            n = sum(islice(dice, 3))
            rolls += 3
            ps[p] = (ps[p]+n)%N
            ss[p] += ps[p]+1
            if ss[p] >= 1000:
                return ss[(p+1)%2] * rolls
print(run())

SPLITS = Counter(map(sum,product(range(1, 3+1), repeat=3))).most_common()
wins = [0, 0]
queue = deque([((0, 0), 0, (*PS,), 1)])
while queue:
    SS, P, PS, U = queue.popleft()
    for dn, du in SPLITS:
        u = U * du
        p = (PS[P]+dn)%N
        s = SS[P]+p+1
        if s >= 21:
            wins[P] += u
        else:
            ss = (SS[0], s) if P else (s, SS[1])
            ps = (PS[0], p) if P else (p, PS[1])
            queue.append((ss, (P+1)%2, ps, u))
print(max(wins))
