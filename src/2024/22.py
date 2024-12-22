import sys

B = list(map(int, sys.stdin))

tt, bananas = 0, {}
for v in B:
    w = tuple([None]*4)
    closed = set()
    for _ in range(2000):
        p = v
        v ^= v*64 % 16777216
        v ^= v//32
        v ^= v*2048 % 16777216

        w = (*w[1:], v%10 - p%10)
        if w not in closed:
            closed.add(w)
            bananas.setdefault(w, 0)
            bananas[w] += v%10
    tt += v

print(tt)
print(max(bananas.values()))
