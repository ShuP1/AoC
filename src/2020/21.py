import sys
from collections import Counter

all_ings = Counter()
table = {}
for line in sys.stdin:
    a, b = line.rstrip(')\n').split(' (contains ')
    ings = a.split(' ')
    alers = b.split(', ')

    for ing in ings:
        all_ings[ing] += 1
    for aler in alers:
        table[aler] = table[aler].intersection(ings) if aler in table else set(ings)

first = lambda c: next(iter(c))
while sum(len(ings) for ings in table.values()) != len(table):
    for aler, ings in table.items():
        if len(ings) == 1:
            ing = first(ings)
            for other in table:
                if aler != other:
                    table[other].discard(ing)

table = {aler: first(table[aler]) for aler in table}

print(sum(all_ings[ing] for ing in all_ings if ing not in table.values()))
print(','.join(ing for _, ing in sorted(table.items())))