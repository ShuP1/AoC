import sys
from hashlib import md5
from itertools import count

key = sys.stdin.readline().strip()
def crack(n):
    for i in count(1):
        m = md5((key + str(i)).encode())
        if m.hexdigest()[:n] == '0'*n:
            return i

print(crack(5))
print(crack(6))
