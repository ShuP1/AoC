import sys
from itertools import count

LINE = *map(int, sys.stdin.readline().split()),

def solve():
    N = len(LINE)
    close = set()
    loop, loop_at = None, 0
    line = list(LINE)
    for n in count(1):
        i = max(range(N), key=lambda i: line[i])
        j = line[i]
        line[i] = 0
        for _ in range(j):
            i = (i+1)%N
            line[i] += 1
        key = tuple(line)
        if key in close:
            if not loop:
                loop = key
                loop_at = n
            elif key == loop:
                return loop_at, n-loop_at
        else:
            close.add(key)

print(*solve(), sep='\n')
