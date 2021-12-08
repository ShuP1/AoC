import sys

lines = sys.stdin.readlines()

"""
 a
b c
 d
e f
 g
"""

p1 = sum([len(digit) in [2, 4, 3, 7] for line in lines for digit in line.strip().split(' | ')[1].split()])
print(p1)

p2 = 0
for line in lines:
    head, tail = line.strip().split(' | ')
    tail = [''.join(sorted(s)) for s in tail.split()]
    digits = {''.join(sorted(s)) for s in (head.split() + tail)}

    mapping = {}
    ln = lambda n: {s for s in digits if len(s) == n}
    tn = lambda l, n, m: (s for s in l if len(set(s) & set(mapping[n])) == m)

    mapping[1], = ln(2)
    mapping[4], = ln(4)
    mapping[7], = ln(3)
    mapping[8], = ln(7)

    l6 = ln(6)
    mapping[6], = tn(l6, 1, 1)
    mapping[9], = tn(l6, 4, 4)
    mapping[0], = l6 - {mapping[6], mapping[9]}

    l5 = ln(5)
    mapping[3], = tn(l5, 1, 2)
    mapping[5], = tn(l5, 6, 5)
    mapping[2], = l5 - {mapping[3], mapping[5]}

    revert = {v: k for k, v in mapping.items()}
    p2 += sum(revert[t] * 10 ** i for i, t in enumerate(reversed(tail)))

print(p2)
