import sys

lines = sys.stdin.readlines()

def solve(p1):
  count = 0
  for line in lines:
    rang, let, pwd = line.split()
    low, high = rang.split('-')

    if p1:
      cnt = pwd.count(let[0])
      if int(low) <= cnt <= int(high):
        count += 1
    else:
      def at(s):
        return pwd[int(s) - 1] == let[0]

      if at(low) != at(high):
        count += 1

  return count

print(solve(True))
print(solve(False))