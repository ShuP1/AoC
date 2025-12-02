import sys

B = [tuple(map(int, s.split('-'))) for s in sys.stdin.readline().strip().split(',')]

p1, p2 = 0, 0
for a, b in B:
    for v in range(a, b + 1):
        s = str(v)
        l = len(s)
        if l % 2 == 0 and s[:l//2] == s[-l//2:]:
            p1 += v
        for n in range(1, l//2 + 1):
            if all(s[i:i+n] == s[:n] for i in range(n, l, n)):
                p2 += v
                break
print(p1)
print(p2)
