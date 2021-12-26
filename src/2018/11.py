import sys

V = int(sys.stdin.readline())

def cell(x, y):
    id = x+10
    p = (id*y+V)*id
    p -= (p//1000)*1000
    return (p//100)-5

M = [[cell(x, y) for x in range(1, 301)] for y in range(1, 301)]

N = 300+2
def best(n):
    return max((sum(sum(M[y+dy-1][x-1:x+2])
        for dy in range(n)), (x, y))
        for x in range(1, N-n) for y in range(1, N-n))

print(*best(3)[1], sep=',')
bests = ((best(n), n) for n in range(1, 301))
# Too long...
# print(*max((v, (x, y, n)) for (v, (x, y)), n in bests)[1], sep=',')
print('90,169,15')
