import sys
import itertools
from functools import reduce
import operator

vals = [int(line) for line in sys.stdin.readlines()]

for part in itertools.combinations(vals, 3):
  if sum(part) == 2020:
    print(reduce(operator.mul, part, 1)) # python 3.8: math.prod
    break