import sys

lines = sys.stdin.readlines()
numbers = [int(v) for v in lines[0].split(',')]

to_grid = lambda g: [[(False, int(v)) for v in l.split()] for l in g[:-1]]
grids = list(map(to_grid, zip(*(iter(lines[2:]),) * 6)))

first = None
last = None
def play(number):
    def inner(grid):
        for row in grid:
            for i, cell in enumerate(row):
                if cell[1] != number:
                    continue

                row[i] = (True, number)
                if all([cell[0] for cell in row]) or all([row[i][0] for row in grid]):
                    global last, first
                    last = sum([sum([v for c, v in row if not c]) for row in grid]) * number
                    if not first:
                        first = last
                    return False
        else:
            return True

    return inner

for number in numbers:
    grids = filter(play(number), grids)

print(first)
print(last)