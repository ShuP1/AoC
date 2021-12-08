import sys
from itertools import permutations

cities = set()
roads = dict()
for line in sys.stdin.readlines():
    road, d = line.split(' = ')
    a, b = road.split(' to ')
    dist = int(d)
    cities.add(a)
    cities.add(b)
    roads[(a, b)] = dist
    roads[(b, a)] = dist

paths = [sum(map(roads.get, zip(cs[:-1], cs[1:]))) \
    for cs in permutations(cities)]
print(min(paths))
print(max(paths))
