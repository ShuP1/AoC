import sys

line = sys.stdin.readline().strip()
N = len(line)

def solve(off):
    return sum(int(n) for i, n in enumerate(line)
        if n == line[(i+off)%N])

print(solve(1))
print(solve(N // 2))
