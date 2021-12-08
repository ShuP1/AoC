import sys
from json import loads

j = loads(sys.stdin.readline())
def count(flt):
    def inner(j):
        t = type(j)
        if t is int:
            return j
        elif t is dict:
            return sum(map(inner, j.values())) if not flt(j) else 0
        elif t is list:
            return sum(map(inner, j))
        else:
            return 0
    return inner(j)

print(count(lambda d: False))
print(count(lambda d: 'red' in d.values()))
