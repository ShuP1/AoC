import sys
import itertools

# (cur, prev)
insts = [(line[0], int(line[1:])) for line in sys.stdin.readlines()]

def apply(s, inst, p2):
  # part 1 ((x, y), dir)
  def move_1(x, y):
    pos = (s[0][0] + x, s[0][1] + y)
    return (pos, s[1])

  def rotate_1(a):
    if a % 90 != 0:
      print('bad angle', a)

    rot = (s[1] + a // 90) % 4
    return (s[0], rot)

  def forward_1(v):
    moves = ['E', 'S', 'W', 'N']
    return apply(s, (moves[s[1]], val), p2)

  # part 2 ((x, y), (wx, wy))
  def move_2(x, y):
    w = (s[1][0] + x, s[1][1] + y)
    return (s[0], w)

  def rotate_2(a):
    if a % 90 != 0:
      print('bad angle', a)

    reverse = a < 0
    w = s[1]
    for _ in range(abs(a) // 90):
      if reverse:
        w = (-w[1], w[0])
      else:
        w = (w[1], -w[0])
    return (s[0], w)

  def forward_2(n):
    pos = (s[0][0] + s[1][0] * n, s[0][1] + s[1][1] * n)
    return (pos, s[1])

  # one more indirection
  move = move_2 if p2 else move_1
  rotate = rotate_2 if p2 else rotate_1
  forward = forward_2 if p2 else forward_1

  (key, val) = inst
  if key == 'N':
    return move(0, val)
  elif key == 'S':
    return move(0, -val)
  elif key == 'E':
    return move(val, 0)
  elif key == 'W':
    return move(-val, 0)
  elif key == 'R':
    return rotate(val)
  elif key == 'L':
    return rotate(-val)
  elif key == 'F':
    return forward(val)
  else:
    print('bad inst', s)
    return s

def solve(state, p2):
  for inst in insts:  # reduce
    state = apply(state, inst, p2)

  print(sum(abs(v) for v in state[0]))

solve(((0, 0), 0), False)
solve(((0, 0), (10, 1)), True)