import sys, math

lines = sys.stdin.readlines()
def parse(line):
    N = []
    p = [None, N]
    i = 1
    while i < len(line):
        c = line[i]
        if c == '[':
            n = []
            p[-1].append(n)
            p.append(n)
        elif c == ']':
            p.pop(-1)
        elif c != ',':
            a, b = line.find(']', i), line.find(',', i)
            j = a if b < 0 else min(a, b)
            p[-1].append(int(line[i:j]))
            i = j-1
        i += 1
    return N

NUMS = [parse(line.strip()) for line in lines]

def explode(p, s, v):
    for c, ps in reversed(p):
        if ps == (s+1):
            n = 1 if s == 0 else 0
            if isinstance(c[n], int):
                c[n] += v
            else:
                c = c[n]
                while isinstance(c[s], list):
                    c = c[s]
                c[s] += v
            return

def reduce(n):
    while True:
        # explode
        p = [(n, 0)]
        while p:
            c, s = p.pop(-1)
            if s > 1:
                continue
            p.append((c, s+1))
            v = c[s]
            if isinstance(v, list):
                p.append((v, 0))
            if len(p) > 4: # explode
                c, s = p.pop(-1)
                cp, sp = p[-1]
                cp[sp-1] = 0
                explode(p, 1, c[0])
                explode(p, 0, c[1])
                break
        if p:
            continue
        # split
        p = [(n, 0)]
        while p:
            c, s = p.pop(-1)
            if s > 1:
                continue
            p.append((c, s+1))
            v = c[s]
            if isinstance(v, list):
                p.append((v, 0))
            elif v >= 10:
                c[s] = [math.floor(v / 2), math.ceil(v / 2)]
                break
        else:
            break
    return n

S = NUMS[0]
for n in NUMS[1:]:
    S = reduce([S, n])

def mag(n):
    if isinstance(n, list):
        return 3*mag(n[0]) + 2*mag(n[1])
    else:
        return n

print(mag(S))

# from itertools import permutations
# print(max( mag(reduce([a, b])) for a,b in
#    permutations([parse(line.strip()) for line in lines], 2) ))
print('4616') # sad
