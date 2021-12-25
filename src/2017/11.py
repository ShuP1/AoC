import sys

DIRS = {
    'n': (0, -1, 1),
    's': (0, 1, -1),
    'nw': (-1, 0, 1),
    'se': (1, 0, -1),
    'sw': (-1, 1, 0),
    'ne': (1, -1, 0)
}

def dist(p):
    return sum(map(abs, p)) // 2

far = 0
p = 0, 0, 0
for d in sys.stdin.readline().strip().split(','):
    p = *(a+b for a,b in zip(p, DIRS[d])),
    far = max(far, dist(p))

print(dist(p))
print(far)
