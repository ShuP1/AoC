import sys

B = [[l.strip() for l in b.split()]
     for b in sys.stdin.read().split('\n\n')]

def solve(smack=0):
    def sym(b):
        for i in range(1, len(b)):
            if sum(u!=v for us,vs in zip(b[i:], b[i-1::-1]) for u,v in zip(us, vs)) == smack:
                return i
        return 0
    return sum(sym(b)*100+sym(list(zip(*b))) for b in B)

print(solve())
print(solve(1))
