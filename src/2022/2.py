import sys

vs = [(ord(a[0])-ord('A'), ord(b[0])-ord('X')) for a,b in
    (l.split(' ') for l in sys.stdin.readlines())]

def play(a, b):
    if a == b:
        return 3
    elif b == (a+1)%3:
        return 6
    else:
        return 0
def score(a, b):
    return b+1+play(a, b)
def to_do(a, b):
    return (a+b-1)%3

print(sum(score(a,b) for a,b in vs))
print(sum(score(a, to_do(a, b)) for a,b in vs))
