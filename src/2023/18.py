import sys

L=[l.strip().split() for l in sys.stdin]

D = {'R': (1,0), 'L': (-1,0), 'D': (0,1), 'U': (0,-1)}
def solve(M):
    x,y = 0,0
    sum1 = 0
    sum2 = 0
    sum_n = 0
    for d, n in M:
        nx, ny = x+D[d][0]*n, y+D[d][1]*n
        sum1 += x * ny
        sum2 += y * nx
        sum_n += n
        x,y = nx,ny
    return round(abs(sum1 - sum2) / 2 + sum_n / 2 + 1)

print(solve((d, int(n)) for d,n,_ in L))
print(solve(('RDLU'[int(c[-2])], int(c[2:-2], base=16)) for _,_,c in L))
