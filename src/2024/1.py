import sys

B = [list(map(int, l.split())) for l in sys.stdin]

ls = list(map(sorted, zip(*B)))
print(sum(abs(a - b) for a,b in zip(*ls)))
print(sum(a * ls[1].count(a) for a in ls[0]))
