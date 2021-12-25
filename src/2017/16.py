import sys

MOVES = sys.stdin.readline().strip().split(',')

N = 16
PS = [chr(ord('a')+i) for i in range(N)]

def step(ps):
    ps = list(ps)
    for move in MOVES:
        m = move[0]
        if m == 's':
            n = int(move[1:])
            ps = [ps[(i-n)%N] for i in range(N)]
        elif m == 'x':
            a, b = *map(int,move[1:].split('/')),
            ps[a], ps[b] = ps[b], ps[a]
        else: # p
            a, b = *map(ps.index, move[1:].split('/')),
            ps[a], ps[b] = ps[b], ps[a]
    return ps

print(''.join(step(PS)))

R = 1_000_000_000
ps = PS
for mod in range(1, R+1):
    ps = step(ps)
    if tuple(ps) == tuple(PS):
        ps = PS # cycle
        for mod in range(R%mod):
            ps = step(ps)
        break
print(''.join(ps))
