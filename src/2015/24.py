import sys
from itertools import combinations

packages = list(map(int, sys.stdin.readlines()))

def run(groups):
    n_p = None
    n_q = float('inf')

    SUM = sum(packages) / groups
    for n in range(1, len(packages)):
        if n_p:
            break
        for ps in combinations(packages, n):
            if sum(ps) == SUM:
                q = 1
                for p in ps: q *= p
                n_p = n
                n_q = min(n_q, q)

    return n_q

print(run(3))
print(run(4))
