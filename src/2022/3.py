import sys

bags = [l.strip() for l in sys.stdin.readlines()]

def priority(v):
    return ord(v)-ord('A')+27 if ord(v)<ord('a') else ord(v)-ord('a')+1

print(sum(priority(v) for bag in bags
    for v in set(bag[:len(bag)//2]) & set(bag[len(bag)//2:])))

print(sum(priority(list(set.intersection(*map(set, bags[i:i+3])))[0])
    for i in range(0, len(bags), 3)))
