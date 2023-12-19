import sys
from math import prod

I,B = ''.join(sys.stdin).strip().split('\n\n')
def inst(s):
    a,*b = s.split(':')
    if not b:
        return (None, a)
    d = '>' in a
    v,n = a.split('<>'[d])
    return ((v, d, int(n)), b[0])
I = {(p := l[:-1].split('{'))[0]: [inst(i) for i in p[1].split(',')] for l in I.split('\n')}
B = [{(q := p.split('='))[0]: int(q[1]) for p in l[1:-1].split(',')} for l in B.split('\n')]

def accept(b):
    w = 'in'
    while w not in 'AR':
        for (v,d,n),x in I[w][:-1]:
            if (d and b[v] > n) or (not d and b[v] < n):
                w = x
                break
        else:
            w = I[w][-1][1]
    return w == 'A'
print(sum(v for b in B if accept(b) for v in b.values()))

K = 'xmas'
def step(v,d,n, rs, inside=True):
    rs = list(rs)
    i = K.index(v)
    l,h = rs[i]
    if d:
        rs[i] = max(l, n+int(inside)),h
    else:
        rs[i] = l,min(h, n-int(inside))
    return rs

ret = 0
q = [('in', ((1,4000), (1,4000), (1,4000), (1,4000)))]
while q:
    w,rs = q.pop()
    if w == 'A':
        ret += prod(h-l+1 for l,h in rs)
    elif w != 'R':
        i = I[w]
        for cond, to in i[:-1]:
            v,d,n = cond
            q.append((to, step(v,d,n, rs)))
            rs = step(v,not d,n, rs, False)
        q.append((i[-1][1], rs))
print(ret)
