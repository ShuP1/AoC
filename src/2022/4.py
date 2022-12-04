import sys

pairs = [tuple(tuple(map(int, p.split('-'))) for p in l.split(','))
    for l in sys.stdin.readlines()]

def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]
def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

print(sum(contains(a, b) or contains(b, a) for a,b in pairs))
print(sum(overlap(a, b) for a,b in pairs))
