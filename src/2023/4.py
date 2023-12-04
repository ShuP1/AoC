import sys

CS = [(set(map(int, (ps := line.split('|'))[0].split()[2:])), list(map(int, ps[1].split()))) for line in sys.stdin.readlines()]

print(sum(2**(sum(h in ws for h in hs)-1) for ws,hs in CS if any(h in ws for h in hs)))

N = [0] * len(CS)
for i,(ws,hs) in enumerate(CS):
    N[i] += 1
    for j in range(sum(h in ws for h in hs)):
        N[i+j+1] += N[i]
print(sum(N))
