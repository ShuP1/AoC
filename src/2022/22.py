import sys
import re

B = sys.stdin.readlines()
B,OP = B[:-2],re.findall(r'\d+|L|R', B[-1])
OP = [int(v) if v.isdigit() else v for v in OP]
Y = len(B)
def get(x,y): return B[y][x] if 0<=y<Y and 0<=x<len(B[y])-1 else ' '

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def solve(wrap):
    x,y,d = B[0].index('.'),0,0
    for op in OP:
        if isinstance(op, int):
            for _ in range(op):
                dx,dy = D[d]
                nx,ny,nd = x+dx,y+dy,d
                if get(nx, ny) == ' ':
                    nx,ny,nd = wrap(x,y,d)
                if get(nx,ny) == '#':
                    break
                x,y,d = nx,ny,nd
        else:
            d += 1 if op == 'R' else -1
            d %= 4
    return (y+1)*1000+(x+1)*4+d

def wrap_plain(x,y,d):
    dx,dy = D[(d+2)%4]
    wx,wy = x+dx,y+dy
    while get(wx,wy) != ' ':
        x,y = wx,wy
        wx,wy = x+dx,y+dy
    return x,y,d

FACES = [
    [0, 1, 2],
    [0, 3, 0],
    [4, 5, 0],
    [6, 0, 0]
]
RIGHT, DOWN, LEFT, UP = range(4)
def wrap_cube(x,y,d):
    x,y,f = x%50, y%50, FACES[y//50][x//50]
    assert f
    _x,_y = x+1,y+1

    if f == 1:
        if d == UP: # to 6
            return 0,x+150,RIGHT
        elif d == LEFT: # to 4
            return 0,151-y,RIGHT
    elif f == 2:
        if d == UP: # to 6
            return x,199,UP
        elif d == DOWN: # to 3
            return 99,x+50,LEFT
        elif d == RIGHT: # to 5
            return 99, 149-y, LEFT
    elif f == 3:
        if d == LEFT: # to 4
            return y,100,DOWN
        elif d == RIGHT: # to 2
            return y+100,49,UP
    elif f == 4:
        if d == UP: # to 3
            return 50,x+50,RIGHT
        elif d == LEFT: # to 1
            return 50,49-y,RIGHT
    elif f == 5:
        if d == RIGHT: # to 2
            return 149,49-y,LEFT
        elif d == DOWN: # to 6
            return 49,x+150,LEFT
    else:
        if d == LEFT: # to 1
            return y+50,0,DOWN
        elif d == RIGHT: # to 5
            return y+50,149,UP
        elif d == DOWN: # to 2
            return x+100,0,DOWN

print(solve(wrap_plain))
print(solve(wrap_cube))
