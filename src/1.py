import sys
import itertools
from functools import reduce
import operator

vals = [int(line) for line in sys.stdin.readlines()]

def solve(n):
  for part in itertools.combinations(vals, n):
    if sum(part) == 2020:
      return reduce(operator.mul, part, 1)  # python 3.8: math.prod

print(solve(2))
print(solve(3))