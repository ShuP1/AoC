import sys
from itertools import permutations

SHEET = [[int(v) for v in line.split()]
    for line in sys.stdin.readlines()]

print(sum(max(row)-min(row) for row in SHEET))
print(sum(next(a // b for a,b in permutations(row, 2) if a%b == 0)
    for row in SHEET))
