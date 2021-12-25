import sys
from itertools import count

JUMPS = *map(int, sys.stdin.readlines()),

def solve(limit=float('inf')):
    jumps = list(JUMPS)
    i = 0
    for n in count():
        if not (0 <= i < len(jumps)):
            return n
        j = jumps[i]
        jumps[i] += 1 if j < limit else -1
        i += j

print(solve())
print(solve(3))
