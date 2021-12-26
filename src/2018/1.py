import sys
from itertools import cycle

lines = *map(int, sys.stdin.readlines()),

print(sum(lines))

s = 0
close = set()
for i in cycle(lines):
    s += i
    if s in close:
        break
    close.add(s)
print(s)
