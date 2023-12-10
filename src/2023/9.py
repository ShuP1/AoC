import sys

I = [[int(n) for n in line.split()] for line in sys.stdin.readlines()]

def solve(r):
    if not any(r):
        return 0
    n = [b-a for a,b in zip(r[:-1], r[1:])]
    return r[-1] + solve(n)

print(sum(map(solve, I)))
print(sum(solve(i[::-1]) for i in I))
