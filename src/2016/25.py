import sys
from itertools import count, islice

lines = sys.stdin.readlines()

A = ord('a')
def toi(c): return ord(c) - A

def run(rs):
    get = lambda c: rs[toi(c)] if c.isalpha() else int(c)
    i = 0
    while i < len(lines):
        ins, rest = lines[i].strip().split(' ', 1)
        i += 1
        if ins == 'cpy':
            x, y = rest.split(' ')
            rs[toi(y)] = get(x)
        elif ins == 'inc':
            rs[toi(rest)] += 1
        elif ins == 'dec':
            rs[toi(rest)] -= 1
        elif ins == 'out':
            yield get(rest)
        else: # jnz
            x, y = rest.split(' ')
            if get(x) != 0:
                i += int(y) - 1

print(next(i for i in count() if all(
    out == (n%2) for n, out in islice(enumerate(run([i, 0, 0, 0])), 50))))
