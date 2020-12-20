import sys

nums = sys.stdin.readline().split(',')

def solve(turns):
  previous = {}
  last = None
  for i, v in enumerate(nums[:-1]):
    previous[int(v)] = i + 1

  last = int(nums[-1])

  for turn in range(len(previous) + 1, turns):
    spoke = 0
    if last in previous:
      spoke = turn - previous[last]

    previous[last] = turn
    last = spoke

  return last

print(solve(2020))
print(solve(30000000))