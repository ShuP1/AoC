import sys
import re

IDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
def ck_hgt(v):
  typ = v[-2:]
  if typ == 'cm':
    return 150 <= int(v[:-2]) <= 193
  elif typ == 'in':
    return 59 <= int(v[:-2]) <= 76
  else:
    return False

CHECKS = {
  'byr': lambda v: 1920 <= int(v) <= 2002,
  'iyr': lambda v: 2010 <= int(v) <= 2020,
  'eyr': lambda v: 2020 <= int(v) <= 2030,
  'hgt': ck_hgt,
  'hcl': re.compile(r"#[0-9a-f]{6}$").match,
  'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': re.compile(r"[0-9]{9}$").match
}

inp = sys.stdin.readlines()

def solve(p1):
  valids = 0
  lines = list(iter(inp))
  while lines:
    ids = []
    line = lines.pop(0).rstrip()
    while line:
      for pair in line.split():
        key, val = pair.split(':')
        if key in CHECKS and (p1 or CHECKS[key](val)):
            ids.append(key)
      if lines:
        line = lines.pop(0).rstrip()
      else:
        line = ''
    if len(IDS.intersection(ids)) == len(IDS):
      valids += 1

  return valids

print(solve(True))
print(solve(False))