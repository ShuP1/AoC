import sys

def parse(line):
    x, y = 0, 0
    res = []
    for inst in line.split(','):
        d = inst[0]
        cnt = int(inst[1:])
        if d == 'U':
            dx, dy = 0, 1
        elif d == 'D':
            dx, dy = 0, -1
        elif d == 'R':
            dx, dy = 1, 0
        elif d == 'L':
            dx, dy = -1, 0
        else:
            print(d)
        for _ in range(cnt):
            x += dx
            y += dy
            res.append((x, y))

    return res

a = parse(sys.stdin.readline().strip())
b = parse(sys.stdin.readline().strip())
c = set(a).intersection(set(b))

print(min(abs(x) + abs(y) for x, y in c))
print(min(a.index(p) + b.index(p) + 2 for p in c))