import sys

I = sys.stdin.readline().strip().split(',')

def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v = v * 17 % 256
    return v
print(sum(map(h, I)))

boxes = [dict() for _ in range(256)]
for s in I:
    l, *f = s.strip('-').split('=')
    b = boxes[h(l)]
    if f:
        b[l] = int(f[0])
    else:
        b.pop(l, 0)
print(sum(i*j*f for i,b in enumerate(boxes, 1) for j,f in enumerate(b.values(), 1)))
