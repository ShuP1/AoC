import sys
from collections import defaultdict
from itertools import product
from functools import partial

lines = sys.stdin.readlines()
ALGO = [c == '#' for c in lines[0].strip()]
IMG = [[c == '#' for c in line.strip()]
    for line in lines[2:]]

def a2i(cs):
    return int(''.join('1' if c else '0'
        for c in cs), 2)
def kernel(img, x, y):
    return ALGO[a2i(img[(x+dx, y+dy)]
        for dy in range(-1, 2)
        for dx in range(-1, 2))]

def solve(N):
    img = defaultdict(int,
        dict.fromkeys(((x, y) for y, row in enumerate(IMG)
            for x, v in enumerate(row) if v), 1))

    low, high = 0, len(IMG[0])
    for i in range(N):
        low -= 1
        high += 1
        new = defaultdict(partial(lambda q: int(q % 2 == 0), q=i) 
            if ALGO[0] == 1 and ALGO[511] == 0 else int)
        for y, x in product(range(low, high), repeat=2):
            new[(x, y)] = int(kernel(img, x, y))
        img = new

    return sum(img.values())

print(solve(2))
print(solve(50))
