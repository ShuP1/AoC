import sys

ings = []
for line in sys.stdin.readlines():
    name, rest = line.strip().split(': ')
    ings.append([int(v.split(' ')[1]) for v in rest.split(', ')])

def ratios(n, s):
    if n <= 1:
        yield [s]
    else:
        for i in range(s+1):
            for j in ratios(n-1, s-i):
                j.append(i)
                yield j

LEN = len(ings)
PRS = 4
CUPS = 100

p1, p2 = 0, 0
for ratio in ratios(LEN, CUPS):
    m = 1
    for i in range(PRS):
        m *= max(0, sum(map(lambda j: ings[j][i] * ratio[j], range(LEN))))

    p1 = max(p1, m)
    if sum(map(lambda j: ings[j][PRS] * ratio[j], range(LEN))) == 500:
        p2 = max(p2, m)

print(p1)
print(p2)
