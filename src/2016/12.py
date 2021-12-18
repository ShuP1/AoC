import sys

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
        else: # jnz
            x, y = rest.split(' ')
            if get(x) != 0:
                i += int(y) - 1
    return rs[0]

print(run([0, 0, 0, 0]))
print(run([0, 0, 1, 0]))
