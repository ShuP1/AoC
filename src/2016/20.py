import sys

BLOCKED = [(*map(int, line.split('-')),) for line in sys.stdin.readlines()]

allowed = 0
ip = 0
while ip <= 4294967295:
    for a,b in BLOCKED:
        if a <= ip <= b:
            ip = b+1
            break
    else:
        if not allowed:
            print(ip) # p1
        allowed += 1
        ip += 1
print(allowed)
