import sys, math

LOOK, _, *NET = sys.stdin.readlines()
LOOK = LOOK.strip()
NET = {line[:3]: (line[7:10], line[12:15]) for line in NET}

def path(node, pred):
    dist = 0
    while not pred(node):
        dir = LOOK[dist % len(LOOK)] == 'R'
        node = NET[node][dir]
        dist += 1
    return dist

print(path('AAA', lambda n: n == 'ZZZ'))
p2 = 1
for node in NET:
    if node.endswith('A'):
        dist = path(node, lambda n: n.endswith('Z'))
        p2 = math.lcm(p2, dist)
print(p2)
