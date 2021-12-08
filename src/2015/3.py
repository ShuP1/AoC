import sys

line = sys.stdin.readline()

def run(line, houses):
    x, y = (0, 0)
    houses.add((x, y))
    for c in line:
        if c == '>':
            x += 1
        elif c == '<':
            x -=1
        elif c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        else:
            print(y, file=sys.stderr)

        houses.add((x, y))

houses = set()
run(line, houses)
print(len(houses))

houses = set()
run(line[0::2], houses)
run(line[1::2], houses)
print(len(houses))
