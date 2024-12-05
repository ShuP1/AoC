import sys

A,B = sys.stdin.read().split('\n\n')
def split(ls, sep):
    return [list(map(int, l.split(sep))) for l in ls.split()]
A,B = split(A, '|'), split(B, ',')

def valid_(bs, a):
    u,v = a
    return u not in bs or v not in bs \
        or bs.index(u) < bs.index(v)
def valid(bs):
    return all(valid_(bs, a) for a in A)
def mid(bs): return bs[len(bs)//2]

print(sum(map(mid, filter(valid, B))))

def fix(bs):
    while not valid(bs):
        for uv in A:
            if not valid_(bs, uv):
                u,v = uv
                i,j = bs.index(u), bs.index(v)
                bs[i],bs[j] = bs[j], bs[i]
    return bs

print(sum(mid(fix(bs)) for bs in B if not valid(bs)))
