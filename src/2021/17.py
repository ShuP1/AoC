import sys
from itertools import product

parts = sys.stdin.readline().split()
XA, XB = map(int, parts[2][2:-1].split('..'))
YA, YB = map(int, parts[3][2:].split('..'))

T = abs(YA) - 1
print(T * T - (T - 1) * T // 2) 

total = 0
for dx, dy in product(range(1, XB + 1), range(YA, abs(YA))):
    x, y = 0, 0
    for _ in range(2 * abs(YA) + 1):
        x += dx
        y += dy
        dx = max(dx - 1, 0)
        dy -= 1

        if YA <= y <= YB and XA <= x <= XB:
            total += 1
            break
        elif y < YA or x > XB:
            break
print(total)
