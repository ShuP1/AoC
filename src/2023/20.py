import sys
from math import prod, lcm
from collections import deque

B = {(p := l.strip().split(' -> '))[0][1:]: (l[0], p[1].split(', ')) for l in sys.stdin}
I = 'broadcaster'
B[I] = (None, B.pop(I[1:])[1])

def rev(t): return [k for k, (_, ds) in B.items() if t in ds]
def state():
    s = {k: False for k, (t, _) in B.items() if t == '%'}
    s.update({k: {j: False for j in rev(k)} for k, (t, _) in B.items() if t == '&'})
    return s

def click(s, fn):
    q = deque([(I, False, None)])
    while q:
        k, h, frm = q.popleft()
        fn(k, h)
        if k not in B:
            continue
        t, ds = B[k]
        if t == '%':
            if not h:
                f = s[k] = not s[k]
                for d in ds:
                    q.append((d, f, k))
        elif t == '&':
            m = s[k]
            m[frm] = h
            n = not all(m.values())
            for d in ds:
                q.append((d, n, k))
        else:
            for d in ds:
                q.append((d, h, k))

counts = [0, 0]
def inc(_, h): counts[h] += 1

s = state()
for _ in range(1000):
    click(s, inc)
print(prod(counts))


to_rx, = rev('rx')
assert B[to_rx][0] == '&'

revs = rev(to_rx)
assert all(B[k][0] == '&' for k in revs)

i = 0
cycles = {}
def check(k, h):
    if k in revs and not h and k not in cycles:
        cycles[k] = i

s = state()
while len(cycles) < len(revs):
    i += 1
    click(s, check)
print(lcm(*cycles.values()))
