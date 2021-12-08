import sys

lines = sys.stdin.readlines()

def run(rs):
    i = 0
    while i < len(lines):
        ins, rest = lines[i].strip().split(' ', 1)
        i += 1
        if ins == 'hlf':
            rs[rest == 'b'] //= 2
        elif ins == 'tpl':
            rs[rest == 'b'] *= 3
        elif ins == 'inc':
            rs[rest == 'b'] += 1
        elif ins == 'jmp':
            i += int(rest) - 1
        else:
            r, off = rest.split(', ')
            v = rs[r == 'b']
            if (ins == 'jie' and v % 2 == 0) or (ins == 'jio' and v == 1):
                i += int(off) -1
    return rs[1]

print(run([0, 0]))
print(run([1, 0]))
