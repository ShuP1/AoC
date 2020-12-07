import sys

lines = sys.stdin.readlines()

def parse_group(lines):
  group = []
  for chars in lines:
    line = chars.strip()
    if line:
      group.append(line)
    else:
      yield group
      group = []
  yield group

anyone = [set().union(*group) for group in parse_group(lines)]
print(sum(map(len, anyone)))
everyone = [set(group[0]).intersection(*group[1:]) for group in parse_group(lines)]
print(sum(map(len, everyone)))