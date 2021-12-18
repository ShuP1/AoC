import sys
from hashlib import md5

KEY = sys.stdin.readline().strip()

N = 4
E = N-1
def doors(x, y, path):
    h = md5((KEY + path).encode()).hexdigest()
    def open(n): return ord(h[n]) > ord('a')
    if y > 0 and open(0):
        yield x, y-1, path+'U'
    if y < E and open(1):
        yield x, y+1, path+'D'
    if x > 0 and open(2):
        yield x-1, y, path+'L'
    if x < E and open(3):
        yield x+1, y, path+'R'

first, last = None, None
queue = [(0, 0, '')]
while queue:
    for door in doors(*queue.pop(0)):
        x, y, path = door
        if x == E and y == E:
            if not first:
                first = path
            last = path
        else:
            queue.append(door)

print(first)
print(len(last))
