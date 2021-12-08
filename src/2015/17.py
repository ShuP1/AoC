import sys
from itertools import combinations

lines = [int(v) for v in sys.stdin.readlines()]

p1, p2 = 0, 0
low = float('inf')
for n in range(len(lines)):
    for c in combinations(lines, n):
        if sum(c) == 150:
            p1 += 1
            if n < low:
                low = n
                p2 = 0
            if n == low:
                p2 += 1

print(p1)
print(p2)
