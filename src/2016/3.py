import sys
from itertools import permutations

lines = [(*map(int, line.strip().split()),) for line in sys.stdin.readlines()]
verts = [p for g in zip(*(lines[i::3] for i in range(3))) for p in zip(*g)]

def valid(p): return all(a+b > c for a,b,c in permutations(p))

print(sum(map(valid, lines)))
print(sum(map(valid, verts)))
