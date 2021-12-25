import sys

line = sys.stdin.readline().strip()

N = 256
def hash(lgs, rounds=1):
    nums = list(range(N))
    i, s = 0, 0
    for _ in range(rounds):
        for l in lgs:
            for m in range(l//2):
                a, b = (i+m)%N, (i+l-m-1)%N
                nums[a], nums[b] = nums[b], nums[a]
            i += l+s
            s += 1
    return nums

p1 = hash(map(int,line.split(',')))
print(p1[0]*p1[1])

def xor(vs):
    acc = 0
    for v in vs:
        acc ^= v
    return acc
def hexa(v):
    return hex(v//16)[2:]+hex(v%16)[2:]

sparse = hash((*map(ord, line), 17, 31, 73, 47, 23), 64)
print(''.join(hexa(xor(sparse[i:i+16]))
    for i in range(0, len(sparse), 16)))
