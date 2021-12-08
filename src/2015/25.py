import sys

parts = sys.stdin.readline().split()
row, col = int(parts[15][:-1]), int(parts[17][:-1])

i, j = 1, 1
val = 20151125
while True:
    if j == 1:
        j = i + 1
        i = 1
    else:
        i += 1
        j -= 1
    val = (val * 252533) % 33554393

    if i == col and j == row:
        print(val)
        break
