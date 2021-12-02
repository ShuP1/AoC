import sys

lines = sys.stdin.readlines()

def solve1():
    x, y = 0, 0
    for line in lines:
        dir, cnt = line.split(' ')
        count = int(cnt)
        if dir == 'forward':
            y += count
        elif dir == 'down':
            x += count
        elif dir == 'up':
            x -= count
        else:
            print('bad dir', dir)

    return x * y

def solve2():
    x, y, aim = 0, 0, 0
    for line in lines:
        dir, cnt = line.split(' ')
        count = int(cnt)
        if dir == 'forward':
            y += count
            x += count * aim
        elif dir == 'down':
            aim += count
        elif dir == 'up':
            aim -= count
        else:
            print('bad dir', dir)

    return x * y

print(solve1())
print(solve2())