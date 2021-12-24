import sys

lines = sys.stdin.readlines()

def vm(rs, input):
    W = ord('w')
    def toi(c): return ord(c) - W
    get = lambda c: rs[toi(c)] if c.isalpha() else int(c)
    for line in lines:
        parts = line.strip().split()
        ins = parts[0]
        r = toi(parts[1])
        v = get(parts[2]) if len(parts) > 2 else None
        if ins == 'inp':
            rs[r] = input.pop(-1)
        elif ins == 'add':
            rs[r] += v
        elif ins == 'mul':
            rs[r] *= v
        elif ins == 'div':
            rs[r] //= v
        elif ins == 'mod':
            rs[r] %= v
        else: # eql
            rs[r] = int(rs[r] == v)
    return rs

def part(inp, z, a, b, c):
    x = int((z % 26 + b) != inp)
    z /= a
    z *= (25 * x) + 1
    z += (inp + c) * x
    return z

groups = (i for i, line in enumerate(lines) if line.strip() == 'inp w')
STEPS = [(*(int(lines[i+j].split()[2]) for j in [4, 5, 15]),) for i in groups]
I = len(STEPS)

def solve(cache, i, z, bonus=False):
    if i >= I:
        return z, None
    k = i, z
    if k in cache:
        return cache[k], None
    
    for x in (range(1, 10) if bonus else range(9, 0, -1)):
        nz = part(x, z, *STEPS[i])
        cache[(i, z)] = nz

        sz, sv = solve(cache, i + 1, nz, bonus)
        if sz == 0:
            v = sv or []
            v.insert(0, x)
            return sz, v
    else:
        return z, None

# Way too slow, solve in rust...
# res = solve(dict(), 0, 0)[1]
# assert vm([0, 0, 0, 0], res)[3] == 0
# print(''.join(res))
# print(''.join(solve(dict(), 0, 0, True)[1]))
print('79197919993985\n13191913571211')
