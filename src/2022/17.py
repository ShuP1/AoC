import sys

LINE = sys.stdin.readline().strip()
L = len(LINE)

SHAPES = [[
    '####'
], [
    '.#.',
    '###',
    '.#.'
], [
    '..#',
    '..#',
    '###'
], [
    '#',
    '#',
    '#',
    '#'
], [
    '##',
    '##'
]]
S = len(SHAPES)

def blocks(s, x, y):
    for dy, row in enumerate(reversed(SHAPES[s%S])):
        for dx, c in enumerate(row):
            if c == '#':
                yield x+dx, y+dy

X = 7
def sim(N):
    g, gh = [], 0
    skips = dict()
    l = 0
    def valid(s, x, y):
        return all(0<=tx<X and ty >= 0 and (ty >= len(g) or g[ty][tx] != '#')
            for tx, ty in blocks(s, x, y))

    s = 0
    while s < N:
        x, y = 2, 3+len(g) # left, bottom
        while True:
            #gas
            tx = x + (-1 if LINE[l] == '<' else 1)
            l = (l+1)%L
            if valid(s, tx, y):
                x = tx
            #fall
            ty = y - 1
            if valid(s, x, ty):
                y = ty
            else:
                break
        for tx, ty in blocks(s, x, y):
            for y in range(len(g), ty+1):
                g.append(['.']*X)
            g[ty][tx] = '#'
        #print('\n'.join(''.join(row) for row in reversed(g)), '\n')
        s += 1
        # skipper
        k = s%S,l
        h = len(g)
        if h > 10000 and k in skips:
            _s,_h = skips[k]
            ds,dh = s-_s,h-_h
            n = (N-s)//ds
            s += n*ds
            gh += n*dh
        else:
            skips[k] = s,h
    return len(g)+gh

print(sim(2022))
print(sim(1000000000000))
