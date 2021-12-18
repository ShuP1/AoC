import sys

I = int(sys.stdin.readline())

p = 1
while p < I:
    p *= 2
print(2 * (I % (p // 2)) + 1)

p = 1
while p < I:
    p *= 3
m = p // 3
print((I // (2 * m) + 2 * (I // (3 * m))) * m + (I // m) * (I % m))
