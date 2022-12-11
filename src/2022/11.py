import sys
from copy import deepcopy
from math import prod

I = []
C = []
for monkey in ''.join(sys.stdin.readlines()).split('\n\n'):
    _,it,op,*ms = monkey.splitlines()
    I.append(list(map(int, it.split(':')[1].split(','))))
    op = ''.join(op.split()[-3:])
    ms = (int(m.split(' ')[-1]) for m in ms)
    C.append((lambda old,op=op: eval(op),*ms))

MOD=prod(cnd for _,cnd,*_ in C)
def run(turn, div):
    M = deepcopy(I)
    N = [0] * len(M)
    for _ in range(turn):
        for i in range(len(M)):
            op,cnd,*to = C[i]
            for item in M[i]:
                N[i] += 1
                item = op(item)
                if div:
                    item //= 3
                else:
                    item %= MOD
                M[to[int(item % cnd != 0)]].append(item)
            M[i].clear()
    return prod(sorted(N)[-2:])

print(run(20, True))
print(run(10000, False))
