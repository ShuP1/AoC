import sys
from collections import defaultdict

state = defaultdict(lambda: 0)
for v in map(int,sys.stdin.readline().split(',')):
    state[v] += 1

def run(steps):
    global state
    for _ in range(steps):
        next = defaultdict(lambda: 0)
        for k, v in state.items():
            if k > 0:
                next[k-1] += v
            else:
                next[8] += v
                next[6] += v
        state = next
    print(sum(state.values()))

run(80)
run(256-80)
