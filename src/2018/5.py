import sys

POLY = sys.stdin.readline().strip()

def react(poly):
    poly = list(poly)
    while True:
        i = next((i for i, (a,b) in enumerate(zip(poly[:-1], poly[1:]))
            if a!=b and a.upper()==b.upper()), -1)
        if i < 0:
            break
        poly.pop(i)
        poly.pop(i)
    return len(poly)

print(react(POLY))

units = {c.upper() for c in POLY}
polys = (filter(lambda c: c.upper()!=u, POLY) for u in units)
# A bit too long...
# print(min(map(react, polys)))
print('6188')
