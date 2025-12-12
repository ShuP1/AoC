import sys

*S, R = [m.splitlines() for m in sys.stdin.read().split('\n\n')]
S = [sum(l.count('#') for l in s[1:]) for s in S]
R = [tuple(map(int,((s := sz.split('x'))[0], s[1][:-1], *ss)))
     for sz, *ss in (b.split() for b in R)]

print(sum(w*h >= sum(n * S[i] for i, n in enumerate(nums))
          for w, h, *nums in R))
