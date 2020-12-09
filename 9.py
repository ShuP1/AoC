import sys
import itertools

vals = [int(line) for line in sys.stdin.readlines()]

preamble = [val for val in vals[:25]]

invalid = None
for val in vals[25:]:
  if any([a + b == val for a, b in itertools.combinations(set(preamble), 2)]):
    preamble.pop(0)
    preamble.append(val)
  else:
    invalid = val
    break

print(invalid)

for r in range(2, len(vals)):
  for i in range(len(vals) - r + 1):
    part = vals[i: i + r]
    if sum(part) == invalid:
      print(min(part) + max(part))
      break
  else: # propagate break
    continue
  break