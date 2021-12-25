import sys
from itertools import product

KEY = sys.stdin.readline().strip()

def xor(vs):
    acc = 0
    for v in vs:
        acc ^= v
    return acc
def hash(key):
    L = (*map(ord, key), 17, 31, 73, 47, 23)
    N = 256
    nums = list(range(N))
    i, s = 0, 0
    for _ in range(64):
        for l in L:
            for m in range(l//2):
                a, b = (i+m)%N, (i+l-m-1)%N
                nums[a], nums[b] = nums[b], nums[a]
            i += l+s
            s += 1
    dense = (xor(nums[i:i+16]) for i in range(0, N, 16))
    return [bool(d >> i & 1) for d in dense for i in reversed(range(8))]

M = 128
GRID = [hash(KEY + '-' + str(i)) for i in range(M)]
print(sum(sum(row) for row in GRID))

groups = []
for p in product(range(M), repeat=2):
    y, x = p
    if GRID[y][x] and not any(p in g for g in groups):
        close = set([p])
        queue = [p]
        while queue:
            y, x = queue.pop()
            for dx,dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x+dx, y+dy
                p = ny, nx
                if 0 <= x < M and 0 <= y < M and GRID[y][x] and p not in close:
                    close.add(p)
                    queue.append(p)
        groups.append(close)
print(len(groups))
