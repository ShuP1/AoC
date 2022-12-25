import sys

n = sum(sum(('=-012'.index(c)-2)*(5**i)
    for i,c in enumerate(reversed(l.strip())))
    for l in sys.stdin.readlines())
s = ''
while n:
    rem = n % 5
    s += str(rem ) if rem <= 2 else '=-'[rem-3]
    n //= 5
    n += rem // 3
print(s[::-1])
