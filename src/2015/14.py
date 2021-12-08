import sys

reindeers = []
for reindeer in sys.stdin.readlines():
    parts = reindeer.split(' ')
    reindeers.append((int(parts[3]), int(parts[6]), int(parts[13])))

pos = [0] * len(reindeers)
cnt = [t for s, t, p in reindeers]
pnt = [0] * len(reindeers)

for _ in range(2503):
    for i, reindeer in enumerate(reindeers):
        s, t, p = reindeer
        if cnt[i] < 0:
            cnt[i] += 1
            if cnt[i] == 0:
                cnt[i] = t
        else:
            pos[i] += s
            cnt[i] -= 1
            if cnt[i] == 0:
                cnt[i] = -p
    m = max(pos)
    for i in range(len(reindeers)):
        if pos[i] == m:
            pnt[i] += 1

print(max(pos))
print(max(pnt))
