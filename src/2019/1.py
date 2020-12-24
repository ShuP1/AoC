import sys
import math

lines = sys.stdin.readlines()

fuel = lambda x: math.floor(x / 3) - 2
print(sum(fuel(int(line)) for line in lines))

total = 0
for line in lines:
    add = fuel(int(line))
    while add > 0:
        total += add
        add = fuel(add)

print(total)