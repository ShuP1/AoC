import sys

B = [l.strip() for l in sys.stdin]
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

kinds = dict()
for y, l in enumerate(B):
    for x, c in enumerate(l):
        kinds.setdefault(c, set()).add((x, y))
plots = []
for ps in kinds.values():
    while ps:
        comp = set()
        q = [ps.pop()]
        while q:
            p = q.pop()
            comp.add(p)
            x, y = p
            for dx, dy in DIRS:
                np = x + dx, y + dy
                if np in ps:
                    q.append(np)
                    ps.remove(np)
        plots.append(comp)

def peri(vs):
    return sum(
        (x + dx, y + dy) not in vs
        for x, y in vs
        for dx, dy in DIRS)
print(sum(len(ps) * peri(ps) for ps in plots))

def sides(vs):
    total = 0
    for x, y in vs:
        mns = sum(
            (x + dx, y + dy) not in vs
            for dx, dy in DIRS)
        if mns == 4:
            total += 4
        elif mns == 3:
            total += 2
        elif mns == 2 and not (
            (x + 1, y) in vs and (x - 1, y) in vs or
            (x, y + 1) in vs and (x, y - 1) in vs
        ):
            total += 1

        if (x + 1, y - 1) not in vs and (x + 1, y) in vs and (x, y - 1) in vs:
            total += 1
        if (x + 1, y + 1) not in vs and (x + 1, y) in vs and (x, y + 1) in vs:
            total += 1
        if (x - 1, y - 1) not in vs and (x - 1, y) in vs and (x, y - 1) in vs:
            total += 1
        if (x - 1, y + 1) not in vs and (x - 1, y) in vs and (x, y + 1) in vs:
            total += 1
    return total
print(sum(len(ps) * sides(ps) for ps in plots))
