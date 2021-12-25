import sys

S = int(sys.stdin.readline())

b = [0]
p = 0
for l in range(1, 2018):
    p = (p+S)%l+1
    b.insert(p, l)
print(b[p+1])

n = 0
p = 0
for l in range(1,50_000_001):
    p = (p+S)%l
    if p == 0:
        n = l
    p += 1
print(n)
