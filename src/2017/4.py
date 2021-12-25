import sys

PHRASES = (line.strip().split() for line in sys.stdin.readlines())

valids = [ws for ws in PHRASES if len(set(ws)) == len(ws)]
print(len(valids))

valids = [ws for ws in valids if len(set(str(sorted(w)) for w in ws)) == len(ws)]
print(len(valids))
