import sys
from itertools import product

B = [l.strip() for l in sys.stdin]
Y, X = len(B), len(B[0])

def access(B=B):
    return [(y, x)
        for y, x in product(range(Y), range(X))
            if B[y][x] == '@' and 5 > sum(B[y + dy][x + dx] == '@'
                for dy, dx in product([-1, 0, 1], repeat=2)
                if 0 <= y + dy < Y and 0 <= x + dx < X)
    ]

print(len(access()))

p2 = 0
b = [list(l) for l in B]
while True:
    changes = access(b)
    if not changes:
        break
    p2 += len(changes)
    for y, x in changes:
        b[y][x] = '.'
print(p2)
