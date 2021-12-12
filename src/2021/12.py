import sys
from collections import defaultdict

links = defaultdict(list)
for line in sys.stdin.readlines():
    a,b = line.strip().split('-')
    if a != 'start':
        links[b].append(a)
    if b != 'start':
        links[a].append(b)

def is_big(c): return c.isupper()

def visit(bonus):
    done = set()
    queue = [('start', [], bonus)]
    while queue:
        at, path, bonus = queue.pop(-1)
        if at == 'end':
            done.add((*path, at))
        else:
            path = path + [at]
            for c in links[at]:
                p2 = bonus
                if is_big(c):
                    pass
                elif p2 and path.count(c) == 1:
                    p2 = False
                elif c in path:
                    continue
                queue.append((c, path, p2))

    return len(done)

print(visit(False))
print(visit(True))
