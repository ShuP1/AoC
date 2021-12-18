import sys

LINE = sys.stdin.readline().strip()

def step(a):
    return a + '0' + ''.join('1' if c == '0' else '0' for c in reversed(a))

def checksum(disk):
    c = ''.join('1' if a == b else '0' for a,b in zip(disk[::2], disk[1::2]))
    if len(c) % 2:
        return c
    else:
        return checksum(c)

def solve(n):
    a = LINE
    while len(a) < n:
        a = step(a)
    return checksum(a[:n])

print(solve(272))
print(solve(35651584))
