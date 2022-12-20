import sys
from collections import deque

lines = list(map(int, sys.stdin.readlines()))
L = len(lines)

def solve(lines, N=1):
    file = deque(list(enumerate(lines)))
    for _ in range(N):
        for frm, num in enumerate(lines):
            to = next(i for i,(j,_) in enumerate(file) if j==frm)
            file.rotate(-to)
            file.popleft()
            file.rotate(-num)
            file.appendleft((frm, num))
    zero = next(i for i,(_,n) in enumerate(file) if n==0)
    return sum(file[(zero+(i+1)*1000)%L][1]
        for i in range(3))

print(solve(lines))
print(solve([n*811589153 for n in lines], N=10))
