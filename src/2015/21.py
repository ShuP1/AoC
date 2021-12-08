import sys
from itertools import combinations, product
from operator import itemgetter
from math import ceil

E = [int(line.split(': ')[1]) for line in sys.stdin.readlines()]
M_H = 100

# Name Cost Damage Armor
WS = [
    ('Dagger', 8, 4, 0),
    ('Shortsword', 10, 5, 0),
    ('Warhammer', 25, 6, 0),
    ('Longsword', 40, 7, 0),
    ('Greataxe', 74, 8, 0)
]
AS = [
    ('Leather', 13, 0, 1),
    ('Chainmail', 31, 0, 2),
    ('Splintmail', 53, 0, 3),
    ('Bandedmail', 75, 0, 4),
    ('Platemail', 102, 0, 5)
]
RS = [
    ('Damage +1', 25, 1, 0),
    ('Damage +2', 50, 2, 0),
    ('Damage +3', 100, 3, 0),
    ('Defense +1', 20, 0, 1),
    ('Defense +2', 40, 0, 2),
    ('Defense +3', 80, 0, 3)
]
EMPTY = ('', 0, 0, 0)

def win(m, e):
    def ttl(a, b):
        return ceil(a[0] / max(1, b[1] - a[2]))
    return ttl(m, e) >= ttl(e, m)

min_win = float('inf')
max_lose = 0
for w, a, rs in product(WS, [EMPTY] + AS, combinations([EMPTY, EMPTY] + RS, 2)):
    inv = (w, a) + rs
    cost, dmg, arm = (sum(map(itemgetter(i), inv)) for i in range(1, 4))
    if win((M_H, dmg, arm), E):
        min_win = min(min_win, cost)
    else:
        max_lose = max(max_lose, cost)

print(min_win)
print(max_lose)
