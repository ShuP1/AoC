import sys
import math

depart = int(sys.stdin.readline())
line2 = sys.stdin.readline()
buses = [int(b) for b in line2.split(',') if b != 'x']

min_i = None
min_wait = 99999
for bus in buses:
  at = math.ceil(depart / bus) * bus
  wait = at - depart
  if wait < min_wait:
    min_i = bus
    min_wait = wait

print(min_i * min_wait)

nbuses = [(n, int(b)) for n, b in enumerate(line2.split(',')) if b != 'x']
# crt
prod = 1
for _, bus in nbuses:
    prod *= bus
time = 0
for n, bus in nbuses:
    b = prod // bus
    time += (bus - n) * b * pow(b, bus-2, bus)
    time %= prod
print(time)