import sys
from functools import reduce

lines = sys.stdin.readlines()
seeds, *steps = ''.join(lines).split('\n\n')
seeds = list(map(int, seeds.split()[1:]))
steps = [[tuple(map(int, line.split())) for line in step.splitlines()[1:]] for step in steps]

def map_seed(step, seed):
    for d, s, l in step:
        if s <= seed < s + l:
            return seed - s + d
    return seed

print(min(reduce(lambda res, step: (map_seed(step, seed) for seed in res), steps, seeds)))

def map_range(step, rg):
    while len(rg) > 0:
        remain = len(rg)
        for d, s, l in step:
            if s <= rg[0] < s+l:
                off = rg[0] - s
                start = d + off
                new_len = min(l - off, len(rg))
                yield range(start, start+new_len)
                rg = rg[new_len:]
                break
            elif s < rg[0]:
                remain = min(remain, rg[0] - s)
        else:
            yield rg[:remain]
            rg = rg[remain:]

print(min(r.start for s,l in zip(seeds[::2], seeds[1::2]) for r in reduce(lambda res, step:
    (v for rg in res for v in map_range(step, rg)), steps, [range(s, s+l)])))
