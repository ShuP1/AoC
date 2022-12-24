import sys

lines = sys.stdin.readlines()
X,Y = len(lines[0].strip())-2,len(lines)-2
BLIZY = [{(x-1,1 if c == '>' else -1) for x,c in enumerate(lines[y]) if c in '<>'} for y in range(1,Y+1)]
BLIZX = [{(y-1,1 if row[x] == 'v' else -1) for y,row in enumerate(lines) if row[x] in '^v'} for x in range(1,X+1)]
def free(x,y,t):
    return all((by+t*d)%Y!=y for by,d in BLIZX[x]) and \
        all((bx+t*d)%X!=x for bx,d in BLIZY[y])

F = lines[0].index('.')-1,-1
T = lines[-1].index('.')-1,Y

def path(F=F,T=T,t=0):
    q = set([F])
    while q:
        c = set()
        t += 1
        for x,y in q:
            for dx,dy in [(0,1),(1,0),(0,0),(0,-1),(-1,0)]:
                tx,ty = x+dx,y+dy
                tt = tx,ty
                if tt == T:
                    return t
                if (0<=tx<X and 0<=ty<Y and free(tx,ty,t)) or tt == F:
                    c.add(tt)
        q = c

print(P1:=path())
print(path(t=path(T,F,P1)))
