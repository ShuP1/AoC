import sys
from functools import lru_cache

def fmt(calc):
    return int(calc[0]) if len(calc) == 1 else tuple(calc)
M = {m: fmt(calc.split()) for m, calc in (l.split(': ')
    for l in sys.stdin.readlines())}

OP = {
    '-': lambda a,b: a-b,
    '+': lambda a,b: a+b,
    '/': lambda a,b: a//b,
    '*': lambda a,b: a*b
}

@lru_cache
def solve(k):
    calc = M[k]
    if isinstance(calc, int):
        return calc
    else:
        a,op,b = calc
        return OP[op](solve(a), solve(b))
print(solve('root'))

LOP = {
    '-': lambda a,b: -a+b,
    '+': lambda a,b: a-b,
    '/': lambda a,b: b//a,
    '*': lambda a,b: a//b
}
ROP = {
    **LOP,
    '-': lambda a,b: a+b,
    '/': lambda a,b: a*b
}

del M['humn']
a,_,b = M['root']
try:
    known = solve(b)
    cur = a
except:
    known = solve(a)
    cur = b
while cur in M:
    a,op,b = M[cur]
    try:
        known = LOP[op](known, solve(a))
        cur = b
    except:
        known = ROP[op](known, solve(b))
        cur = a
print(known)
