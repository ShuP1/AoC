import sys
from collections import defaultdict

orbited = defaultdict(list)
orbits = defaultdict(list)
for line in sys.stdin:
    a, b = line.strip().split(')')
    orbited[a].append(b)
    orbits[b].append(a)

cnt = 0
for obj in orbits:
    while obj != 'COM':
        cnt += 1
        obj = orbits[obj][0]

print(cnt)

def path(start, end):
    mark = {}
    mark[start] = 0
    queue = [start]
    while queue:
        cur = queue.pop(0)
        icur = mark[cur]
        if cur == end:
            return icur

        for o in orbits[cur] + orbited[cur]:
            if o not in mark:
                mark[o] = icur + 1
                queue.append(o)

    return None


print(path(orbits['YOU'][0], orbits['SAN'][0]))