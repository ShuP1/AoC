import sys

PORTS = set((*map(int, line.split('/')),) for line in sys.stdin.readlines())

p1 = 0
p2 = len(PORTS), 0
queue = [(0, 0, PORTS)]
while queue:
    n, s, ps = queue.pop()
    p1 = max(p1, s)
    if len(ps) - (s > p2[1]) < p2[0]:
        p2 = len(ps), s
    for p in ps:
        a,b = p
        ns = s+a+b
        if a == n:
            queue.append((b, ns, ps-{p}))
        elif b == n:
            queue.append((a, ns, ps-{p}))
print(p1)
print(p2[1])
