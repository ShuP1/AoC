import sys
from itertools import product
from math import prod

lines = sys.stdin.readlines()

ons = set()
for line in lines:
    mode, rng = line.split()
    rng = (map(int,ax[2:].split('..')) for ax in rng.split(','))
    new = set(product(*(range(max(-50, a), min(b+1, 50+1)) for a,b in rng)))
    if mode == 'on':
        ons.update(new)
    else:
        ons.difference_update(new)
print(len(ons))


def size(axs):
    return prod(ax[1]-ax[0] for ax in axs)

def intersects(to, other):
    return all(ax[0] <= bx[1]-1 and bx[0] <= ax[1]-1
        for ax, bx in zip(to, other))
def contains(to, other):
    return all(ax[0] <= bx[0] and ax[1] >= bx[1]
        for ax, bx in zip(to, other))

def subtract(to, other):
    if not intersects(to, other):
        return [to]
    elif contains(other, to):
        return []

    axs = (zip(ax, ax[1:]) for ax in (sorted((*ax, *bx)) for ax, bx in zip(to, other)))
    return [cube for cube in product(*axs)
        if contains(to, cube) and not intersects(cube, other)]

cubes = []
for line in lines:
    mode, rng = line.split()
    axs = (ax[2:].split('..') for ax in rng.split(','))
    step = *((int(ax[0]), int(ax[1])+1) for ax in axs),
    cubes = [part for cube in cubes
        for part in subtract(cube, step)]
    if mode == 'on':
        cubes.append(step)

print(sum(map(size, cubes)))
