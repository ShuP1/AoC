import sys
from functools import cache

B = {f[:-1]: ts for f, *ts in (l.strip().split() for l in sys.stdin)}

@cache
def paths(f, t):
    return 1 if f == t else sum(paths(n, t) for n in B.get(f, []))

print(paths('you', 'out'))
print((paths('svr', 'fft') * paths('fft', 'dac') * paths('dac', 'out')) +
    (paths('svr', 'dac') * paths('dac', 'fft') * paths('ftt', 'out')))
