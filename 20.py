import sys
import math
import itertools
from collections import Counter, defaultdict

groups = [l.strip() for l in sys.stdin.read().split('\n\n') if l.strip()]

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def fmt(self): return '\n'.join(self.grid)
    @staticmethod
    def join(line): return ''.join(line)

    def line(self, i): return self.grid[i]
    def column(self, i):
        return Grid.join(row[i] for row in self.grid)

    def flip(self):
        return Grid(list(reversed(self.grid)))

    def rotate(self):
        return Grid([self.column(i) for i in reversed(range(len(self.grid)))])

    def edges(self):
        return [self.line(0), self.line(-1), self.column(-1), self.column(0)]

    def all_dirs(self):
        cur = self
        for _ in range(4):
            yield cur
            yield cur.flip()
            cur = cur.rotate()

    def core(self):
        return [x[1:-1] for x in self.grid[1:-1]]

    def count(self, s):
        return Grid.join(self.grid).count(s)

tiles = {}
for group in groups:
    lines = group.split('\n')
    i = int(lines[0][5:-1])
    tiles[i] = Grid([l.strip() for l in lines[1:]])

ds = defaultdict(list)
for i, grid in tiles.items():
    for brd in grid.edges():
        ds[brd].append(i)
        ds[Grid.join(reversed(brd))].append(i)

brds = Counter()
for ups in ds.values():
    if len(ups) > 1:
        for up in ups:
            brds[up] += 1

# just an heuristic
min_v = 99
min_ks = []
min_prod = 1
for k, v in brds.items():
    if v == min_v:
        min_ks.append(k)
        min_prod *= k
    elif v < min_v:
        min_ks = [k]
        min_v = v
        min_prod = k

assert min_v == 4 and len(min_ks) == 4
print(min_prod)

# part 2
N = int(math.sqrt(len(tiles)))

monster = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

start_corner = min_ks[0]
start_grid = tiles[start_corner]
while len(ds[start_grid.column(0)]) == 2:
    start_grid = start_grid.rotate()

def find(other, edge, get_edge):
    me = next(me for me in ds[edge] if me != other)
    return next((me, grid) for grid in tiles[me].all_dirs() if edge == get_edge(grid))

# build grid by row
pos_grid = [[None] * N for _ in range(N)]
pos_grid[0][0] = (start_corner, start_grid)
for y in range(0, N):
    if y > 0:
        ln, ln_grid = pos_grid[y-1][0]
        pos_grid[y][0] = find(ln, ln_grid.line(-1), get_edge=lambda g: g.line(0))

    for x in range(1, N):
        ln, ln_grid = pos_grid[y][x-1]
        pos_grid[y][x] = find(ln, ln_grid.column(-1), get_edge=lambda g: g.column(0))

pic = []
for row in pos_grid:
    part = [''] * len(row[0][1].core())
    for _, col in row:
        for i, line in enumerate(col.core()):
            part[i] += line
    pic += part

# count monster in correct orientation
nb_monsters = 0
for pic in Grid(pic).all_dirs():
    nb_monsters = 0
    grid = pic.grid
    for my in range(len(grid)-len(monster)):
        for mx in range(len(grid)-len(monster[0])):
            is_monster = True
            for y in range(len(monster)):
                for x in range(len(monster[y])):
                    if monster[y][x] == '#' and grid[my+y][mx+x] != '#':
                        is_monster = False
                        break
                if not is_monster:
                    break

            if is_monster:
                nb_monsters += 1

    if nb_monsters:
        break

print(pic.count('#') - Grid(monster).count('#') * nb_monsters)