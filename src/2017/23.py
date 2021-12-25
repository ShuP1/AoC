import sys
from collections import defaultdict

lines = sys.stdin.readlines()

def vm():
    p1 = 0
    rs = defaultdict(int)
    get = lambda c: rs[c] if c.isalpha() else int(c)
    i, I = 0, len(lines)
    while i < I:
        parts = lines[i].strip().split()
        i += 1
        ins = parts[0]
        r = parts[1]
        v = get(parts[2]) if len(parts) > 2 else None
        if ins == 'set':
            rs[r] = v
        elif ins == 'sub':
            rs[r] -= v
        elif ins == 'mul':
            p1 += 1
            rs[r] *= v
        else: # jnz
            if get(r) != 0:
                i += v - 1
    return p1

print(vm())

# Reverse code
def is_prime(n):
    return all((n % i) != 0 for i in range(2, n//2))

N = int(lines[0].split()[-1])
b = (N*100)+100000
c = b+17000
h = 0
while True:
    if not is_prime(b):
        h += 1
    if b == c:
        break
    b += 17
print(h)
