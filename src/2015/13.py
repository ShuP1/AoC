import sys
from collections import defaultdict
from itertools import permutations

guests = defaultdict(dict)
for line in sys.stdin.readlines():
    who, rest = line.strip().split(' would ')
    parts = rest.split(' ')
    v = int(parts[1])
    if parts[0] == 'lose':
        v *= -1
    guests[who][parts[8][:-1]] = v

NG = len(guests)
def happiness(seat):
    def flt(i):
        who = guests[seat[i]]
        return who[seat[(i-1)%NG]] \
             + who[seat[(i+1)%NG]]
    return sum(map(flt, range(NG)))

def run():
    print(max(map(happiness, permutations(guests.keys()))))

run()
for guest in list(guests.keys()):
    guests['You'][guest] = 0
    guests[guest]['You'] = 0
NG += 1
run()
