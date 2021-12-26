import sys
from collections import defaultdict

L = set()
G = defaultdict(set)
for line in sys.stdin.readlines():
    p = line.split()
    a,b = p[1], p[7]
    L.add(a)
    L.add(b)
    G[b].add(a)

started = ''
done = set()
def ready(s):
    return s not in started and all(g in done for g in G[s])

while len(started) < len(L):
    s = min(filter(ready, L))
    started += s
    done.add(s)
print(started)

def time(t):
    return 61+ord(t)-ord('A')

W = 5
started = ''
done = set()
NULL = chr(ord('Z')+1)
workers = [[0, NULL] for _ in range(W)]
workers[0][1] = '?'
while len(started) < len(L):
    w = min(w for w in workers if w[1] != NULL)
    t = w[0]
    done.add(w[1])
    w[1] = NULL

    while True:
        w = next((w for w in workers if w[1] == NULL), None)
        s = min(*filter(ready, L), NULL)
        if not w or s == NULL:
            break
        started += s
        w[0] = t+time(s)
        w[1] = s
print(max(workers)[0])
