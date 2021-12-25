import sys
from itertools import count

lines = sys.stdin.readlines()
DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

word = ''
d = 1
x, y = lines[0].index('|'), 1
for i in count(1):
    c = lines[y][x]
    if c.isalpha():
        word += c
    elif c == ' ':
        break
    elif c == '+':
        ds = ((nd, DS[nd]) for nd in range(4) if nd != (d+2)%4)
        cs = ((d, lines[y+dy][x+dx]) for d, (dx, dy) in ds)
        d = next(d for d, c in cs if c == ('-' if d%2==0 else '|'))
    dx, dy = DS[d]
    x += dx
    y += dy
print(word)
print(i)
