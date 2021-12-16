import sys
from math import prod

line = sys.stdin.readline().strip()
nums = (ord(c) - (ord('0') if c < 'A' else ord('A')-10) for c in line)
BITS = [x & 1 << n != 0 for x in nums for n in reversed(range(4))]

def bs2i(bs):
    return int(''.join('1' if b else '0' for b in bs), 2)
def get(i, n):
    return i+n, bs2i(BITS[i:i+n])

OPS = [
    sum, prod, min, max, None,
    lambda vs: int(vs[0] > vs[1]),
    lambda vs: int(vs[0] < vs[1]),
    lambda vs: int(vs[0] == vs[1])
]

p1 = 0
def parse(i, I, limit=float('inf')):
    global p1
    cnt = 0
    buf = []
    while i < I-7 and cnt < limit:
        i, v = get(i, 3)
        p1 += v
        i, type = get(i, 3)
        if type == 4:
            bs = BITS[i+1:i+5]
            while BITS[i]:
                i += 5
                bs += BITS[i+1:i+5]
            i += 5
            buf.append(bs2i(bs))
        else:
            i += 1
            if BITS[i-1]:
                i, n = get(i, 11)
                i, args = parse(i, I, n)
            else:
                i, n = get(i, 15)
                i, args = parse(i, i+n)
            buf.append(OPS[type](args))
        cnt += 1
    return i, buf

_, ret = parse(0, len(BITS))
print(p1)
print(*ret)
