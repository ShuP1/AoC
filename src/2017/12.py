import sys

lines = (line.strip().split(' <-> ') for line in sys.stdin.readlines())
PIPES = {int(p): set(map(int, r.split(', '))) for p,r in lines}

groups = []
for i in range(max(PIPES.keys())+1):
    if any(i in g for g in groups):
        continue
    close = set([i])
    queue = [i]
    while queue:
        for p in PIPES[queue.pop()]:
            if p not in close:
                close.add(p)
                queue.append(p)
    groups.append(close)
print(len(groups[0]))
print(len(groups))
