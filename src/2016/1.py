import sys

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

x, y, dir = 0, 0, 0
close = set((x, y))
twice = None
for line in sys.stdin.readline().split(', '):
    t, d = line[:1], int(line[1:])
    dir += 1 if t == 'R' else -1
    dir %= len(DIR)
    dx, dy = DIR[dir]
    for _ in range(d):
        x += dx
        y += dy
        if not twice:
            p = (x, y)
            if p in close:
                twice = p
            else:
                close.add(p)

def card(x, y): return abs(x) + abs(y)
print(card(x, y))
print(card(*twice))
