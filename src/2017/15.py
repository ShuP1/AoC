import sys
from itertools import islice

STARTS = [int(line.split()[4]) for line in sys.stdin.readlines()]

def generator(v, f):
    while True:
        v = (v*f)%2147483647
        yield v

A = lambda: generator(STARTS[0], 16807)
B = lambda: generator(STARTS[1], 48271)

def matches(A, B, n):
    MASK = (1<<16)-1
    return sum(a&MASK == b&MASK for a,b in islice(zip(A, B), n))

def zeros(g, n):
    MASK = (1<<n)-1
    return filter(lambda v: v&MASK == 0, g)

print(matches(A(), B(), 40_000_000))
print(matches(zeros(A(), 2), zeros(B(), 3), 5_000_000))
