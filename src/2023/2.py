import sys
from math import prod

games = {
    int((h := line.split(':'))[0][5:]):
    [{(p := v.split())[1]: int(p[0]) for v in s.split(',')}
        for s in h[1].split(';')]
    for line in sys.stdin.readlines()
}

BAG = {'red': 12, 'green': 13, 'blue': 14}
print(sum(i for i,logs in games.items() if all(all(BAG[c] >= v for c,v in log.items()) for log in logs)))
print(sum(prod(max(log.get(c, 0) for log in logs) for c in BAG) for logs in games.values()))
