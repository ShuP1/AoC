import sys
from collections import Counter

lines = sys.stdin.readlines()
distribution = [Counter(line[i] for line in lines).most_common() for i in range(len(lines[0].strip()))]

print(''.join(c[0][0] for c in distribution))
print(''.join(c[-1][0] for c in distribution))
