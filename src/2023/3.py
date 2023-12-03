import sys
from collections import defaultdict

lines = sys.stdin.readlines()
Y, X = len(lines), len(lines[0].strip())

p1 = 0
geared = defaultdict(list)
for y in range(Y):
    gears = set()
    n = 0
    has_part = False
    for x in range(X+1):
        if x<X and lines[y][x].isdigit():
            n = n*10+int(lines[y][x])
            for y2 in range(max(0, y-1), min(Y, y+2)):
                for x2 in range(max(0, x-1), min(X, x+2)):
                    ch = lines[y2][x2]
                    if not ch.isdigit() and ch != '.':
                        has_part = True
                    if ch=='*':
                        gears.add((y2, x2))
        elif n>0:
            for gear in gears:
                geared[gear].append(n)
            if has_part:
                p1 += n
            n = 0
            has_part = False
            gears.clear()

print(p1)
print(sum(v[0]*v[1] for v in geared.values() if len(v)==2))
