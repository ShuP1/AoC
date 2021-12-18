import sys
from collections import Counter

def rotate(n):
    A = ord('a')
    N = ord('z') - A + 1
    return lambda c: chr((ord(c) - A + n) % N + A)

TARGET = 'northpole object storage'

p1 = 0
p2 = None
for line in sys.stdin.readlines():
    parts = line.strip().split('-')
    sector = int(parts.pop(-1)[:3])

    check = sorted(Counter(''.join(parts)).items(), key=lambda t: (-t[1], t[0]))
    check = ''.join(c for c,_ in check[:5])
    if check != line[-7:-2]:
        continue

    p1 += sector
    name = ' '.join(''.join(map(rotate(sector), part)) for part in parts)
    if name == TARGET:
        p2 = sector

print(p1)
print(p2)
