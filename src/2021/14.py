import sys
from collections import Counter

lines = sys.stdin.readlines()
TPL = lines[0].strip()
PAIRS = dict(line.strip().split(' -> ')
    for line in lines[2:])

def solve(limit):
    pairs = Counter(TPL[i:i + 2]
        for i in range(0, len(TPL) - 1))

    for _ in range(limit):
        new_pairs = Counter()
        cnt = Counter()
        for k, v in pairs.items():
            new_pairs[k[0] + PAIRS[k]] += v
            new_pairs[PAIRS[k] + k[1]] += v
            cnt[k[0]] += v
            cnt[PAIRS[k]] += v
        pairs = new_pairs
    cnt[TPL[-1]] += 1

    cnt = cnt.most_common()
    return cnt[0][1] - cnt[-1][1]

print(solve(10))
print(solve(40))
