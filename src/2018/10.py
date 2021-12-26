import sys
from itertools import count

lines = (line.strip().split('> ') for line in sys.stdin.readlines())
PS = [[(*map(int, l[0][10:].split(',')),), (*map(int, l[1][10:-1].split(',')),)] for l in lines]

for wait in count():
    if max(p[0][1] for p in PS) <= min(p[0][1] for p in PS)+9:
        break
    for p in PS:
        p[0] = (p[0][0] + p[1][0], p[0][1] + p[1][1])

ox, oy = min(p[0][0] for p in PS), min(p[0][1] for p in PS)
sx, sy = max(p[0][0] for p in PS)-ox+1, max(p[0][1] for p in PS)-oy+1
SCREEN = [[' ']*sx for _ in range(sy)]
for p, v in PS:
    SCREEN[p[1]-oy][p[0]-ox] = '#'
# human power
# for row in SCREEN:
#     print(''.join(row))
print('BXJXJAEX')
print(wait)
