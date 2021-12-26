import sys

STARS = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

def near(a, b):
    return sum(abs(va-vb) for va,vb in zip(a, b)) <= 3

cons = 0
close = set()
for s in STARS:
    if s not in close:
        con = set([s])
        queue = [s]
        while queue:
            s = queue.pop()
            for t in STARS:
                if t not in close and near(s, t):
                    close.add(t)
                    con.add(t)
                    queue.append(t)
        cons += 1
print(cons)
