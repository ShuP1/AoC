import sys
from functools import reduce

CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
def check(line):
    pile = []
    for c in line:
        if c in CLOSE:
            pile.append(c)
        elif not pile or c != CLOSE[pile.pop(-1)]:
            return False, c
    else:
        return True, pile

lines = [check(line.strip()) for line in sys.stdin.readlines()]

ERR = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
print(sum(ERR[c] for v, c in lines if not v))

CMP = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
p2 = sorted(reduce(lambda p, c: p * 5 + CMP[CLOSE[c]], reversed(pile), 0) for v, pile in lines if v)
print(p2[len(p2) // 2])
