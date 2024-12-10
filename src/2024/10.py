import sys

B = [list(map(int, l.strip())) for l in sys.stdin]
Y,X = len(B),len(B[0])

def trails(opn, nxt, add):
    for i in range(1, 10):
        nxt.clear()
        for x,y in opn:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx,y+dy
                if 0 <= nx < X and 0 <= ny < Y and B[ny][nx] == i:
                    add(nxt, (nx,ny))
        opn,nxt = nxt,opn
    return len(opn)
def solve(new, add):
    return sum(trails(new([(x,y)]), new(), add)
        for y, l in enumerate(B) for x, v in enumerate(l) if not v)

print(solve(set, lambda s, v: s.add(v)))
print(solve(list, lambda l, v: l.append(v)))
