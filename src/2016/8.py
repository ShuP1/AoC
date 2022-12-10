import sys, os
from itertools import product
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ocr import ocr_array

lines = sys.stdin.readlines()
X, Y = 50, 6
screen = [['.']*X for _ in range(Y)]

for line in lines:
    parts = line.strip().split()
    if parts[0] == 'rect':
        a, b = map(int, parts[1].split('x'))
        for x, y in product(range(a), range(b)):
            screen[y][x] = '#'
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

print(sum(v == '#' for row in screen for v in row))
print(ocr_array(screen))
