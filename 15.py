import sys
import math
import itertools

nums = sys.stdin.readline().split(',')

previous = {}
last = None
for i, v in enumerate(nums[:-1]):
  previous[int(v)] = i + 1

last = int(nums[-1])


for turn in range(len(previous) + 1, 30000000): # part 1: 2020
  spoke = 0
  if last in previous:
    spoke = turn - previous[last]

  previous[last] = turn
  last = spoke

print(last)