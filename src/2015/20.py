import sys
from itertools import count
from math import ceil, sqrt

target = int(sys.stdin.readline())

def divisors(n):
    d = set()
    d.add(1)
    d.add(n)
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            d.add(i)
            d.add(n / i)
    return d

a, b = None, None
for n in count(1):
    ds = divisors(n)
    if not a:
        t = sum(ds) * 10
        if t >= target:
            a = n
            if b:
                break
    if not b:
        t = sum(filter(lambda d: d * 50 >= n, ds)) * 11
        if t >= target:
            b = n
            if a:
                break

print(a)
print(b)
