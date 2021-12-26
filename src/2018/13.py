import sys

SAMPLE = ['/->-\\',
          '|   |  /----\\',
          '| /-+--+-\\  |',
          '| | |  | v  |',
          '\\-+-/  \\-+--/',
          '  \\------/']
lines = sys.stdin.readlines()

DS = {
    'v': {
        '|': ('v', (0, 1)),
        '/': ('<', (-1, 0)),
        '\\': ('>', (1, 0)),
        'l': ('>', (1, 0)),
        's': ('v', (0, 1)),
        'r': ('<', (-1, 0))
    },
    '^': {
        '|': ('^', (0, -1)),
        '/': ('>', (1, 0)),
        '\\': ('<', (-1, 0)),
        'l': ('<', (-1, 0)),
        's': ('^', (0, -1)),
        'r': ('>', (1, 0))
    },
    '>': {
        '-': ('>', (1, 0)),
        '/': ('^', (0, -1)),
        '\\': ('v', (0, 1)),
        'l': ('^', (0, -1)),
        's': ('>', (1, 0)),
        'r': ('v', (0, 1))
    },
    '<': {
        '-': ('<', (-1, 0)),
        '/': ('v', (0, 1)),
        '\\': ('^', (0, -1)),
        'l': ('v', (0, 1)),
        's': ('<', (-1, 0)),
        'r': ('^', (0, -1))
    }
}
INTS = {
    'l': 's',
    's': 'r',
    'r': 'l',
}

TRAINS = {(x, y): (c, 'l') for y, line in enumerate(lines)
    for x, c in enumerate(line) if c in '<>^v'}
TRACK = {(x, y): ('|' if c in '^v' else ('-' if c in '<>' else c))
    for y, line in enumerate(lines)
    for x, c in enumerate(line) if c != ' '}

def step(trains, no_crash):
    for p in sorted(trains, key=lambda p: (p[1], p[0])):
        if p not in trains:
            continue

        d, mem = trains.pop(p)
        rail = TRACK[p]
        if rail == '+':
            rail = mem
            mem = INTS[mem]
        d, mv = DS[d][rail]
        p = p[0]+mv[0], p[1]+mv[1]
        t = (d, mem)

        if p not in trains:
            trains[p] = t
        elif no_crash:
            trains.pop(p)
        else:
            return p
    return None

def solve(no_crash=False):
    trains = dict(TRAINS)
    r = None
    while r is None and len(trains) > 1:
        r = step(trains, no_crash)
    return r or next(iter(trains))

print(*solve(), sep=',')
print(*solve(True), sep=',')
