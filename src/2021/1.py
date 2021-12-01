import sys

vals = [int(line) for line in sys.stdin.readlines()]

def solve(window):
    return sum([vals[i+window] > vals[i] for i in range(len(vals)-window)])

print(solve(1))
print(solve(3))