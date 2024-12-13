import sys

B = [tuple(int(s[2:].rstrip(',')) for s in (ax,ay,bx,by,px,py))
     for _,_,ax,ay,_,_,bx,by,_,px,py in
     map(str.split, ''.join(sys.stdin).split('\n\n'))]

def solve(b, offset=0):
    ax, ay, bx, by, px, py = b

    det = ax * by - ay * bx
    if det == 0:
        return 0

    px += offset
    py += offset

    na = by * px - bx * py
    nb = -ay * px + ax * py
    if na % det or nb % det:
        return 0
    return (na * 3 + nb) // det

print(sum(map(solve, B)))
print(sum(solve(b, 10000000000000) for b in B))
