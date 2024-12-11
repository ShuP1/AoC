import sys
from functools import cache

B = list(map(int, sys.stdin.readline().split()))

def solve(limit):
    @cache
    def rec(v, n=0):
        if n == limit:
            return 1
        n += 1
        if v == 0:
            return rec(1, n)
        s = str(v)
        l = len(s)
        if l % 2 == 0:
            return rec(int(s[:l//2]), n) + rec(int(s[l//2:]), n)
        return rec(v*2024, n)
    return sum(map(rec, B))

print(solve(25))
print(solve(75))
