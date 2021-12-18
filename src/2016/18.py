import sys

LINE = [c == '.' for c in sys.stdin.readline().strip()]
N = len(LINE)

def is_safe(prev, i):
    l, r = tuple(0 <= i+j < N and not prev[i+j] for j in [-1, 1])
    return not (l^r)

def solve(n):
    r = LINE
    t = sum(r)
    for _ in range(n-1):
        r = [is_safe(r, i) for i in range(N)]
        t += sum(r)
    return t

print(solve(40))
print(solve(400000))
