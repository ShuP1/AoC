import sys
import itertools

lines = sys.stdin.readlines()

def getId(line):
  return sum([2 ** (len(line) - 2 - idx) if char in ['B', 'R'] else 0
    for idx, char in enumerate(line.strip())])

seats = list(map(getId, lines))
print("Max seat id:", max(seats))

for seat in seats:
  my_seat = seat + 1
  next_seat = my_seat + 1
  if my_seat not in seats and next_seat in seats:
    print("Free seat id:", my_seat)