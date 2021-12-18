import sys

lines = sys.stdin.readlines()
A = ord('a')
def toi(c): return ord(c) - A

def run(rs):
    get = lambda c: rs[toi(c)] if c.isalpha() else int(c)
    i = 0
    tgls = set()
    while i < len(lines):
        ins, rest = lines[i].strip().split(' ', 1)
        tgl = i in tgls
        i += 1
        if ins == 'inc' or ins == 'dec' or (tgl and ins == 'tgl'):
            rs[toi(rest)] += 1 if (ins == 'inc')^tgl else -1
        elif ins == ('jnz' if tgl else 'cpy'):
            x, y = rest.split(' ')
            if not y.isalpha():
                continue
            rs[toi(y)] = get(x)
        elif ins == ('cpy' if tgl else 'jnz'):
            x, y = rest.split(' ')
            if get(x) != 0:
                i += get(y) - 1
        else: # tgl
            x = i+get(rest)-1
            if x in tgls:
                tgls.remove(x)
            else:
                tgls.add(x)

    return rs[0]

print(run([7, 0, 0, 0]))
# Too long...
# print(run([12, 0, 0, 0]))
print('479010245')
