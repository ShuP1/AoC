import sys

n1, n2 = 0, 0
for line in sys.stdin.readlines():
    same = lambda c: c[0] == c[1]
    if len([c for c in line if c in 'aeiou']) >= 3 and \
       all([not (v in line) for v in ['ab', 'cd', 'pq', 'xy']]) and \
       any(map(same, zip(line[:-1], line[1:]))):
        n1 += 1

    if any(map(same, zip(line[:-2], line[2:]))) and \
       any(map(lambda i: line.find(line[i:i+2], i+2) > 0, range(len(line)-1))):
        n2 += 1

print(n1)
print(n2)
