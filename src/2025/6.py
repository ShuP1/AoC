import sys
from operator import add, mul
from functools import reduce

B = [l.rstrip('\n') for l in sys.stdin]

p1 = 0
for *nums, op in zip(*(l.split() for l in B)): 
    p1 += reduce(add if op == '+' else mul, map(int, nums))
print(p1)

p2 = 0
n = 0
fn = add
for *nums, op in zip(*map(list, B)):
    if all(c == ' ' for c in nums):
        continue
    v = int(''.join(nums))
    if op != ' ':
        p2 += n
        fn = add if op == '+' else mul
        n = v
    else:
        n = fn(n, v)
p2 += n
print(p2)
