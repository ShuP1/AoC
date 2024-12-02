import sys

B = [list(map(int, l.split())) for l in sys.stdin]

def safe(l):
    p = list(zip(l[:-1], l[1:]))
    return all(1 <= abs(a-b) <= 3 for a,b in p) and (
        all(a > b for a,b in p) or
        all(a < b for a,b in p))

print(sum(map(safe, B)))
print(sum(safe(l) or any(safe(l[:i] + l[i+1:])
    for i in range(len(l))) for l in B))
