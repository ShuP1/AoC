import sys

paths = []
for chrs in sys.stdin:
    line = chrs.strip()
    # e, se, sw, w, nw, ne
    path = []
    skip = False
    for i in range(len(line)):
        if skip:
            skip = False
            continue

        if line[i] in ['s', 'n']:
            path.append(line[i] + line[i + 1])
            skip = True
        else:
            path.append(line[i])
    paths.append(path)


flipped = set()
for path in paths:
    crds = [0, 0]
    for step in path:
        if step == 'e':
            crds[0] += 1
        elif step == 'w':
            crds[0] -= 1
        elif step == 'ne':
            crds[0] += 1
            crds[1] -= 1
        elif step == 'sw':
            crds[0] -= 1
            crds[1] += 1
        elif step == 'nw':
            crds[1] -= 1
        elif step == 'se':
            crds[1] += 1
        else:
            print(step)
    c = (crds[0], crds[1])
    if c in flipped:
        flipped.remove(c)
    else:
        flipped.add(c)

print(len(flipped))

# part 2
def toset(crd):
    return (crd[0], crd[1])

def is_black(crd):
    return toset(crd) in flipped

def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]

DELTAS = [[0, 1], [0, -1], [1, -1], [-1, 1], [1, 0], [-1, 0]]
def neighbors(crd):
    return sum(1 for d in DELTAS if is_black(add(crd, d)))

def step(flipped):
    result = set()
    for black in flipped:
        for d in [[0, 0]] + DELTAS:
            crd = add(black, d)
            if toset(crd) not in result:
                ns = neighbors(crd)
                if is_black(crd):
                    if 1 <= ns <= 2:
                        result.add(toset(crd))
                else:
                    if ns == 2:
                        result.add(toset(crd))
    return result


for _ in range(100):
    flipped = step(flipped)

print(len(flipped))
