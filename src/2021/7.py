import sys

line = list(map(int,sys.stdin.readline().split(',')))

def cost1(to):
    return sum([abs(v-to) for v in line])

def sum2n(n): return n*(n+1)//2
def cost2(to):
    return sum([sum2n(abs(v-to)) for v in line])

def search(cost):
    h = sum(line)//len(line)
    v = cost(h)

    dir = -1 if cost(h-1) < v else 1
    vn = v

    while vn <= v:
        h += dir
        v, vn = vn, cost(h)
    
    return v

print(search(cost1))
print(search(cost2))
