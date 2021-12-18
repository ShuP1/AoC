import sys
from itertools import count

disks = []
for line in sys.stdin.readlines():
    parts = line.split()
    disks.append((int(parts[1][1:]), int(parts[11][:-1]), int(parts[3])))

def solve(disks):
    return next(t for t in count() if all((t+n+p)%ps == 0
        for n, p, ps in disks))

print(solve(disks))
print(solve(disks + [(len(disks)+1, 0, 11)]))
