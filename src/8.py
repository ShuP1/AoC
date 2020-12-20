import sys
import itertools

lines = sys.stdin.readlines()

def parse(line):
  (inst, num) = line.split(' ')
  return (inst, int(num))

insts = list([parse(line.strip()) for line in lines if line.strip()])

def run():
  path = []
  acc = 0
  ptr = 0

  while ptr not in path and ptr < len(insts):
    path.append(ptr)
    inst = insts[ptr]
    if inst[0] == 'acc':
      acc = acc + inst[1]
      ptr = ptr + 1
    elif inst[0] == 'nop':
      ptr = ptr + 1
    elif inst[0] == 'jmp':
      ptr = ptr + inst[1]
    else:
      print('bad inst at ', ptr)
      return False
  return (acc, ptr)

print(run()[0])

def fixInst(i):
  if insts[i][0] == 'jmp':
    insts[i] = ('nop', insts[i][1])
  elif insts[i][0] == 'nop':
    insts[i] = ('jmp', insts[i][1])
  else:
    return False
  return True

# brute force
for i in range(len(insts)):
  if not fixInst(i):
    continue

  (acc, ptr) = run()
  if ptr >= len(insts):
    print(acc)

  # restore
  fixInst(i)