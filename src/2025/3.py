import sys

B = [tuple(map(int, l.strip())) for l in sys.stdin]

def joltage(l, n=2):
    t = 0
    li = 0
    for n in range(n, 0, -1):
        li = max(range(li, len(l)-(n-1)), key=lambda i: l[i])
        t *= 10
        t += l[li]
        li += 1
    return t

print(sum(map(joltage, B)))
print(sum(map(lambda b: joltage(b, 12), B)))
