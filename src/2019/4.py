import sys
import itertools

start, end = map(int, sys.stdin.readline().strip().split('-'))

def solve(p2):
    cnt = 0
    for i in range(start, end + 1):
        if list(str(i)) != sorted(str(i)):
            continue

        double = False
        for j, js in itertools.groupby(str(i)):
            n = len(list(js))
            if n > 1 and (not p2 or n == 2):
                double = True

        if not double:
            continue

        cnt += 1
    return cnt

print(solve(False))
print(solve(True))