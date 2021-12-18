import sys
from hashlib import md5
from itertools import count, islice

key = sys.stdin.readline().strip()
def cracker(stretching):
    def hash(i):
        h = key + str(i)
        for _ in range(stretching):
            h = md5(h.encode()).hexdigest()
        return h
    N = 1000
    buffer = [hash(i) for i in range(1000)]
    for i in count(0):
        k = buffer.pop(0)
        buffer.append(hash(i+N))
        triple = next((k[i] for i in range(len(k)-2)
            if k[i] == k[i+1] and k[i] == k[i+2]), None)
        if triple:
            fives = 5 * triple
            if any(fives in b for b in buffer):
                yield i, k

def solve(power=0):
    return next(islice(cracker(power+1), 64-1, None))[0]

print(solve())
print(solve(2016))
