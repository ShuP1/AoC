import sys

s1, s2 = 0, 0
for line in sys.stdin.readlines():
    line = line.strip()

    s1 += len(line) - len(eval(line))
    s2 += sum([c in '"\\' for c in line]) + 2

print(s1)
print(s2)
