import sys
from collections import deque

line = sys.stdin.readline().split()
P, L = int(line[0]), int(line[6])

def play(N):
    ps = [0] * P
    ms = deque([0])
    for n in range(1, N+1):
        if n%23:
            for _ in range(2):
                ms.append(ms.popleft())
            ms.appendleft(n)
        else:
            for _ in range(6):
                ms.appendleft(ms.pop())
            ps[(n-1)%P] += n + ms.pop()
    return max(ps)

print(play(L))
print(play(L*100))
