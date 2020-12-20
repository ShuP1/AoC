import sys
import math
import itertools

rules = {}
while True:
  line = sys.stdin.readline().rstrip()
  if not line:
    break

  name, rs = line.split(': ')
  rule1, rule2 = rs.split(' or ')
  s1, e1 = rule1.split('-')
  s2, e2 = rule2.split('-')
  rules[name] = [(int(s1), int(e1)), (int(s2), int(e2))]

assert sys.stdin.readline().startswith("your ticket")
my_ticket = [int(i) for i in sys.stdin.readline().rstrip().split(',')]

sys.stdin.readline()
assert sys.stdin.readline().startswith("nearby tickets")
near_tickets = [[int(i) for i in line.rstrip().split(',')] for line in sys.stdin]

# print(rules, my_ticket, near_tickets)

# part 1
error_rate = 0
valid_tickets = []
for ticket in near_tickets:
  valid = True
  for val in ticket:
    if not any(start <= val <= end for rule in rules.values() for start, end in rule):
      error_rate += val
      valid = False
  if valid:
    valid_tickets.append(ticket)

print(error_rate)

# part 2
orders = [None] * len(my_ticket)
progress = True
while progress:
  progress = False
  for i in range(len(orders)):
    if orders[i] is None:
      valids = [name for name in rules if all(any(start <= ticket[i] <= end for start, end in rules[name]) for ticket in valid_tickets)]
      if len(valids) == 1:
        orders[i] = valids[0]
        del rules[orders[i]]
        progress = True
        break

# print(orders)

def prod(it):
  from functools import reduce
  import operator
  return reduce(operator.mul, it, 1)

print(prod(my_ticket[i] for i, name in enumerate(orders) if name.startswith('departure')))