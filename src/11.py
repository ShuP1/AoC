import sys
import itertools

inp = [line.rstrip() for line in sys.stdin.readlines()]

def solve(p2):
  state = [l for l in inp]
  def countAdj(x, y):
    def isOccupied_1(dx, dy):
      cx = x + dx
      cy = y + dy
      return 0 <= cx < len(state) and 0 <= cy < len(state[cx]) and state[cx][cy] == '#'

    def isOccupied_2(dx, dy):
      cx = x + dx
      cy = y + dy
      while 0 <= cx < len(state) and 0 <= cy < len(state[cx]):
        if state[cx][cy] == '#':
          return True
        elif state[cx][cy] == 'L':
          return False
        cx = cx + dx
        cy = cy + dy
      return False

    isOccupied = isOccupied_2 if p2 else isOccupied_1
    return sum([isOccupied(dx, dy) for dx in range(-1, 1+1) for dy in range(-1, 1+1) if (dx, dy) != (0, 0)])

  def step(prevs):
    curs = [[]] * len(prevs)
    change = False
    for x in range(len(curs)):
      curs[x] = [''] * len(prevs[x])
      for y in range(len(curs[x])):
        prev = prevs[x][y]
        cur = prev
        if prev == 'L':
          if countAdj(x, y) == 0:
            cur = '#'
            change = True
        elif prev == '#':
          if countAdj(x, y) >= (5 if p2 else 4):
            cur = 'L'
            change = True
        curs[x][y] = cur
    return (curs, change)

  change = True
  while change:
    (state, change) = step(state)

  print(sum(sum(cell == '#' for cell in row) for row in state))

solve(False)
solve(True)