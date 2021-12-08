import sys

floor = 0
basement = None
for i, c in enumerate(sys.stdin.readline().strip()):
    floor += 1 if c == '(' else -1
    if not basement and floor < 0:
        basement = i + 1

print(floor)
print(basement)
