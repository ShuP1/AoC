import sys
from itertools import product

lines = sys.stdin.readlines()

NUM1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
NUM2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

DIR = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def run(NUM):
    S = len(NUM)
    x, y = next((x, y) for x, y in product(range(S), repeat=2) if NUM[x][y] == 5)
    num = ''
    for line in lines:
        for c in line.strip():
            dx, dy = DIR[c]
            nx, ny = x + dx, y + dy
            if 0 <= nx < S and 0 <= ny < S and NUM[nx][ny]:
                x, y = nx, ny
        num += str(NUM[x][y])
    return num

print(run(NUM1))
print(run(NUM2))
