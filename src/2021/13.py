import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ocr import ocr_array

lines = sys.stdin.readlines()
sep = lines.index('\n')
dots = {(*map(int, dot.split(',')),) for dot in lines[:sep]}

def fold(dots, line):
    axis, l = line.split()[2].split('=')
    ax_n = int(axis == 'y')
    limit = int(l)

    stable = set(filter(lambda p: p[ax_n] < limit, dots))
    limit *= 2
    return stable.union([(x, limit - y) if ax_n else (limit - x, y)
        for x, y in dots - stable])

code = fold(dots, lines[sep+1])
print(len(code))

for line in lines[sep+2:]:
    code = fold(code, line)

screen = [['.'] * 40 for _ in range(6)]
for x, y in code:
    screen[y][x] = '#'
print(ocr_array(screen))
