import sys
import numpy as np

B = [tuple(map(int, l.strip().replace(' @', ',').split(', '))) for l in sys.stdin]

L,H = 200000000000000,400000000000000
def p1(a, b):
    ax,ay,_,adx,ady,_ = a
    bx,by,_,bdx,bdy,_ = b

    dt = bdx*ady - bdy*adx
    if dt == 0:
        return False

    u = ((by-ay)*bdx - (bx-ax)*bdy) / dt
    v = ((by-ay)*adx - (bx-ax)*ady) / dt
    if u < 0 or v < 0:
        return False

    return L <= bx + bdx * v <= H and L <= by + bdy * v <= H
print(sum(p1(a,b) for i,a in enumerate(B) for b in B[i+1:]))

def eqns(mvx, mvy, mvz):
    u,v = [],[]
    for i,(px,py,pz,vx,vy,vz) in enumerate(B):
        eqn = [1, 0, 0] + [0] * len(B)
        eqn[3+i] = mvx - vx
        u.append(tuple(eqn))
        v.append(px)
        
        eqn = [0, 1, 0] + [0] * len(B)
        eqn[3+i] = mvy - vy
        u.append(tuple(eqn))
        v.append(py)
        
        eqn = [0, 0, 1] + [0] * len(B)
        eqn[3+i] = mvz - vz
        u.append(tuple(eqn))
        v.append(pz)
    return np.matrix(u),np.matrix(v).T

def solve(mvx, mvy, mvz):
    u,v = eqns(mvx, mvy, mvz)
    return float(np.linalg.lstsq(u,v, rcond=None)[1])

vx, vy, vz = 0, 0, 0
cur = solve(vx, vy, vz)
S = 0.0001
LR = 1e-22
fail = 0
near = 0
while near < 10:
    dvx = solve(vx + S, vy, vz) - cur
    dvy = solve(vx, vy + S, vz) - cur
    dvz = solve(vx, vy, vz + S) - cur

    vx -= LR * dvx
    vy -= LR * dvy
    vz -= LR * dvz

    last_score = cur
    cur = solve(vx, vy, vz)
    if cur > last_score:
        fail += 1

    if fail > 5:
        fail = 0
        LR = LR / 2

    if all(((vi + 0.5) % 1) - 0.5 < 0.001 for vi in (vx,vy,vz)):
        near += 1
    else:
        near = 0

u,v = eqns(round(vx), round(vy), round(vz))
res = np.linalg.solve(u[:5,:5], v[:5])
print(round(res[0,0] + res[1,0] + res[2,0]))
