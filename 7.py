import sys
import itertools

lines = sys.stdin.readlines()

def parse(line):
  (source, targets) = line.split(' contain ')
  dests = {}
  for target in targets.strip('.').split(', '):
    (count, name) = target.split(' ', 1)
    try:
      dests[name.rsplit(' ', 1)[0]] = int(count)
    except ValueError as err:
      pass
  return (source.rsplit(' ', 1)[0], dests)

graph = {}
for chars in lines:
  line = chars.strip()
  if line:
    (source, dests) = parse(line)
    graph[source] = dests

queue = [contenant for contenant in graph if 'shiny gold' in graph[contenant]]
sub_graph = list(queue)
while queue:
  bag = queue.pop(0)
  for contenant in graph:
    if contenant not in sub_graph and bag in graph[contenant]:
      queue.append(contenant)
      sub_graph.append(contenant)
print(len(sub_graph))

queue = ['shiny gold']
count = -1 # ignore shiny gold bag itself
while queue:
  bag = queue.pop(0)
  count = count + 1
  content = graph[bag]
  for (next_bag, quantity) in content.items():
    for _ in range(quantity):
      queue.append(next_bag)
print(count)