import sys

B = [l.strip() for l in sys.stdin]
SX, SY = next((x,y) for y, l in enumerate(B) for x, c in enumerate(l) if c == '^')

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def sim(bx=-1,by=-1):
    closed = set()
    x, y, d = SX,SY,0
    while True:
        if (x, y, d) in closed:
            return set()
        closed.add((x, y, d))
        nx, ny = x + DIRS[d][0], y + DIRS[d][1]
        if not (0 <= nx < len(B[0]) and 0 <= ny < len(B)):
            break
        if B[ny][nx] == '#' or (bx == nx and by == ny):
            d = (d + 1) % 4
        else:
            x, y = nx, ny
    return closed

seen = set((x,y) for x,y,_ in sim())
print(len(seen))
print(sum(not sim(x,y) for x,y in seen))
