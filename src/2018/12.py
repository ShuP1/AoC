import sys

lines = sys.stdin.readlines()
POTS = {i for i, c in enumerate(lines[0].strip().split()[2]) if c == '#'}
rules = (line.strip().split(' => ') for line in lines[2:])
RULES = {tuple(c == '#' for c in f) for f, t in rules if t == '#'}

def step(old):
    return { i for i in range(min(old)-3, max(old)+4)
        if tuple(i+j in old for j in range(-2, 3)) in RULES}

pots = POTS
for _ in range(20):
    pots = step(pots)
print(sum(pots))

pots = POTS
N = 50_000_000_000
delta = list(range(10))
last = sum(pots)
for i in range(N):
    pots = step(pots)
    delta[i%10] = sum(pots)-last
    if all(d == delta[0] for d in delta):
        break
    last = sum(pots)
print((N-i)*delta[0]+last)
