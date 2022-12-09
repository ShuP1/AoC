import sys

lines = sys.stdin.readlines()

DIR = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}
def cmp(a, b):
    return (a>b)-(a<b)
def add(*vs):
    return tuple(map(sum, zip(*vs)))

def sim(N):
    q = [(0, 0)] * (N+1)
    seen = set([q[-1]])
    for l in lines:
        d, n = l.split()
        for _ in range(int(n)):
            q[0] = add(q[0], DIR[d])
            for i in range(N):
                u, v = q[i:i+2]
                if any(abs(a-b)>1 for a,b in zip(u,v)):
                    q[i+1] = add(v, (cmp(u[0], v[0]), cmp(u[1], v[1])))
            seen.add(q[-1])
    return len(seen)

print(sim(1))
print(sim(9))

