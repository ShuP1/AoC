import sys
from math import prod, sqrt, floor, ceil

V = [(*map(int, line.split()[1:]),) for line in sys.stdin.readlines()]
def count(run):
    time, dist = run
    dist += 1
    b1 = floor((time + sqrt(pow(time, 2) - 4 * dist))/2)
    b2 = ceil((time - sqrt(pow(time, 2) - 4 * dist))/2)
    return b1 - b2 + 1

print(prod(map(count, zip(*V))))
print(count(int(''.join(map(str, row))) for row in V))
