import sys
from collections import defaultdict
from math import prod

stuff = defaultdict(list)
output = defaultdict(list)
dos = dict()
ready = []

def give(v, to):
    idx = int(to[1])
    if to[0] == 'bot':
        if stuff[idx]:
            ready.append(idx)
        stuff[idx].append(v)
    else:
        output[idx].append(v)

for line in sys.stdin.readlines():
    parts = line.strip().split()
    if parts[0] == 'value':
        give(int(parts[1]), parts[4:])
    else: # bot
        dos[int(parts[1])] = (parts[5:7], parts[10:])

p1 = None
while ready:
    b = ready.pop()
    bot = stuff[b]
    l, h = min(bot), max(bot)
    bot.clear()
    if l == 17 and h == 61:
        p1 = b

    give(l, dos[b][0])
    give(h, dos[b][1])

print(p1)
print(prod(v for i in range(3) for v in output[i]))
