import sys
from itertools import product

lines = sys.stdin.readlines()
X, Y = 50, 6
screen = [[False]*X for _ in range(Y)]

for line in lines:
    parts = line.strip().split()
    if parts[0] == 'rect':
        a, b = map(int, parts[1].split('x'))
        for x, y in product(range(a), range(b)):
            screen[y][x] = True
    else: 
        a = int(parts[2].split('=')[1])
        b = int(parts[4])
        if parts[1] == 'row':
            row = screen[a]
            screen[a] = [row[(i-b)%X] for i in range(X)]
        else: # column
            col = [screen[(i-b)%Y][a] for i in range(Y)]
            for y, v in enumerate(col):
                screen[y][a] = v

print(sum(v for row in screen for v in row))
# print('\n'.join(''.join('#' if v else '.' for v in row) for row in screen), '\n')
print('eoargphyao') # read it, human
