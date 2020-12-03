import sys
import itertools

count = 0
for line in sys.stdin.readlines():
  rang, let, pwd = line.split()
  low, high = rang.split('-')
  """
  # part 1
  cnt = pwd.count(let[0])
  if cnt >= int(low) and cnt <= int(high):
  """
  def at(s):
    return pwd[int(s) - 1] == let[0]

  if at(low) != at(high):
    count = count + 1

print(count)