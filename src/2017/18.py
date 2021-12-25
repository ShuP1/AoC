import sys
from collections import defaultdict, deque

lines = sys.stdin.readlines()

def vm1():
    rs = defaultdict(int)
    snd = None
    get = lambda c: rs[c] if c.isalpha() else int(c)
    i, I = 0, len(lines)
    while i < I:
        parts = lines[i].strip().split()
        i += 1
        ins = parts[0]
        r = parts[1]
        v = get(parts[2]) if len(parts) > 2 else None
        if ins == 'snd':
            snd = get(r)
        elif ins == 'set':
            rs[r] = v
        elif ins == 'add':
            rs[r] += v
        elif ins == 'mul':
            rs[r] *= v
        elif ins == 'mod':
            rs[r] %= v
        elif ins == 'jgz':
            if get(r) > 0:
                i += v - 1
        else: # rcv
            if get(r) != 0:
                return snd
print(vm1())

def vm2():
    cur = [defaultdict(int), 0, deque(), 0]
    oth = [defaultdict(int, {'p': 1}), 0, deque(), 0]
    p1 = oth
    I = len(lines)
    stuck = False
    while cur[1] < I or oth[1] < I:
        if cur[1] >= I:
            cur, oth = oth, cur

        rs = cur[0]
        parts = lines[cur[1]].strip().split()
        cur[1] += 1
        ins = parts[0]
        r = parts[1]
        get = lambda c: cur[0][c] if c.isalpha() else int(c)
        v = get(parts[2]) if len(parts) > 2 else None
        if ins == 'snd':
            cur[2].append(rs[r])
            cur[3] += 1
        elif ins == 'set':
            rs[r] = v
        elif ins == 'add':
            rs[r] += v
        elif ins == 'mul':
            rs[r] *= v
        elif ins == 'mod':
            rs[r] %= v
        elif ins == 'jgz':
            if get(r) > 0:
                cur[1] += v - 1
        else: # rcv
            if oth[2]:
                rs[r] = oth[2].popleft()
            elif stuck:
                break
            else:
                stuck = True
                cur[1] -= 1
                cur, oth = oth, cur
                continue
        stuck = False
    return p1[3]
print(vm2())
