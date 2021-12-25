import sys
from collections import defaultdict

lines = (line.strip().split() for line in sys.stdin.readlines())
INS = [(r, op, (a, b), int(by)*(1 if d=='inc' else -1)) for r,d,by,_,a,op,b in lines]

OPS = {
    '>': lambda a,b: a > b,
    '<': lambda a,b: a < b,
    '>=': lambda a,b: a >= b,
    '<=': lambda a,b: a <= b,
    '==': lambda a,b: a == b,
    '!=': lambda a,b: a != b
}

rs = defaultdict(int)
get = lambda v: rs[v] if v.isalpha() else int(v)
high = 0
for r, op, (a, b), by in INS:
    if OPS[op](get(a), get(b)):
        rs[r] += by
        high = max(high, rs[r])
print(max(rs.values()))
print(high)
