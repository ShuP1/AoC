import sys
from itertools import product

lines = [line.strip() for line in sys.stdin.readlines()]
assert all(len(line) == len(lines[0]) for line in lines[1:])

count = lambda n: sum(any(id.count(c) == n
    for c in id)
    for id in lines)
print(count(2)*count(3))

for p in product(lines, repeat=2):
    diff = [i for i, (a, b) in enumerate(zip(*p)) if a != b]
    if len(diff) == 1:
        w = list(p[0])
        w.pop(diff[0])
        print(''.join(w))
        break
