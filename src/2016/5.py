import sys
from hashlib import md5
from itertools import count, islice

LEN = 8

key = sys.stdin.readline().strip()
def cracker(start, n):
    N = '0'*n
    for i in count(0):
        m = md5((key + str(i)).encode())
        if m.hexdigest()[:n] == N:
            yield i, m
def crack(): return cracker(key, 5)

pwd1 = ''.join(map(lambda t: t[1].hexdigest()[5], islice(crack(), LEN)))
print(pwd1)

pwd2 = [None] * LEN
for _, m in crack():
    p, c = list(m.hexdigest()[5:7])
    p = int(p, base=16)
    if p < LEN and pwd2[p] is None:
        pwd2[p] = c
        if not any(c is None for c in pwd2):
            break
print(''.join(pwd2))
