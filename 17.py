import sys
import math
import itertools

N = 4

def tsum(t1, t2):
  return tuple(map(lambda i, j: i + j, t1, t2))

state = set()
for y, line in enumerate(sys.stdin):
  for x, char in enumerate(line.strip()):
    if char == '#':
      state.add((x, y) + tuple([0] * (N - 2)))
size = (x + 1, y + 1) + tuple([1] * (N - 2))


DELTAS = [delta for delta in itertools.product(range(-1, 2), repeat=N) if any(d != 0 for d in delta)]
def neighbors(pos):
  return sum(tsum(pos, delta) in state for delta in DELTAS)

def debug():
  for high in itertools.product(*map(range, size[2:])):
    print(high)
    for y in range(size[1]):
      print(''.join('#' if (x, y) + high in state else '.' for x in range(size[0])))


def step(size):
  positive = [False] * N
  negative = [False] * N
  result = []
  for pos in itertools.product(*(range(-1, i + 1) for i in size)):
    nbs = neighbors(pos)
    active = pos in state
    if (active and nbs in [2, 3]) or (not active and nbs == 3):
      result.append(pos)
      for i in range(N):
        if pos[i] < 0:
          negative[i] = True
        elif pos[i] >= size[i]:
          positive[i] = True

  return (set(tsum(r, negative) for r in result), tsum(tsum(size, positive), negative))

for cycle in range(6):
  # debug()
  state, size = step(size)
  print(cycle)

print(len(state))