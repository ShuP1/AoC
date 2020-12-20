import sys
import itertools

vals = sorted([int(line) for line in sys.stdin.readlines()])

ones = 1
threes = 1
for i in range(1, len(vals)):
  diff = vals[i] - vals[i - 1]
  if diff == 1:
    ones = ones + 1
  elif diff == 3:
    threes = threes + 1
  else:
    print("bad diff", diff)
  
print(ones * threes)

def countArgs(vals):
  target = vals[-1] + 3
  cache = {}
  def countArg(vals, start):
      key = (len(vals), start)
      if key in cache:
          return cache[key]
      args = 0
      if target - start <= 3:
          args = args + 1
      if vals:
        args = args + countArg(vals[1:], start)
        if vals[0] - start <= 3:
            args = args + countArg(vals[1:], vals[0])
      cache[key] = args
      return args
  return countArg(vals, 0)

print(countArgs(vals))