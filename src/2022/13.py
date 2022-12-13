import sys

lines = sys.stdin.readlines()
pairs = [(eval(a), eval(b)) for a,b in zip(lines[::3], lines[1::3])]

def cmp(a, b):
    return (a>b)-(a<b)
def cmp_r(left, right):
    il, ir = type(left) is int, type(right) is int
    if il and ir:
        return cmp(right, left)
    if il:
        left = [left]
    if ir:
        right = [right]
    for l,r in zip(left, right):
        if (v := cmp_r(l, r)) != 0:
            return v
    return cmp(len(right), len(left))

print(sum(i+1 for i,p in enumerate(pairs) if cmp_r(*p)>0))

i2 = sum(cmp_r(v, [[2]])>0 for p in pairs for v in p)+1
i6 = sum(cmp_r(v, [[6]])>0 for p in pairs for v in p)+2
print(i2*i6)
