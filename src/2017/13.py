import sys
from itertools import count

lines = ((*map(int, line.split(': ')),) for line in sys.stdin.readlines())
MAP = {a: b for a, b in lines}

severity = sum(d*r for d,r in MAP.items()
    if d%(2*(r-1)) == 0)
print(severity)

delay = next(i for i in count() if all(
    (d+i)%(2*(r-1)) != 0 for d,r in MAP.items()))
print(delay)
