import sys

DATA = *map(int, sys.stdin.readline().split()),

p1 = 0
p2 = -1
queue = [[[], DATA[0], DATA[1]]]
i = 2
while queue:
    c = queue[-1]
    cs, n, m = c
    if n > 0:
        c[1] -= 1
        queue.append([[], DATA[i], DATA[i+1]])
        i += 2
    else:
        dt = DATA[i:i+m]
        i += m
        s = sum(dt)
        p1 += s
        if cs:
            s = sum(cs[n-1] for n in dt if n <= len(cs))
        queue.pop()
        if queue:
            queue[-1][0].append(s)
        else:
            p2 = s
print(p1)
print(p2)
