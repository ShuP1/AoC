import sys

lines = sys.stdin.readlines()

screen = [[c == '#' for c in line.strip()] for line in lines]
N = len(screen)

def ngb(cur, ax, ay):
    n = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x, y = ax + dx, ay + dy
            if x >= 0 and y >= 0 and \
               x < N and y < N and \
               cur[x][y]:
                n += 1
    return n

def step(cur):
    next = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            n = ngb(cur, x, y)
            next[x][y] = n == 3 or (n == 4 and cur[x][y])
    return next

def run(edit):
    cur = screen
    for _ in range(100):
        cur = step(edit(cur))
    return sum(map(sum, edit(cur)))

def force(cur):
    cur[0][0] = True
    cur[0][N-1] = True
    cur[N-1][0] = True
    cur[N-1][N-1] = True
    return cur

print(run(lambda c: c))
print(run(force))
