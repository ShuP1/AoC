import sys

g = [[(False, 0)] * 1000 for _ in range(1000)]
for line in sys.stdin.readlines():
    parts = line.split(' ')
    if parts[0] == 'turn':
        parts.pop(0)

    ins = parts[0]
    xa, ya = map(int, parts[1].split(','))
    xb, yb = map(int, parts[3].split(','))
    for x in range(xa, xb+1):
        r = g[x]
        for y in range(ya, yb+1):
            if ins == 'on':
                r[y] = (True, r[y][1]+1)
            elif ins == 'off':
                r[y] = (False, max(0, r[y][1]-1))
            else:
                a, b = r[y]
                r[y] = (not a, b+2)

def cnt(n):
    return sum(sum(v[n] for v in r) for r in g)

print(cnt(0))
print(cnt(1))
