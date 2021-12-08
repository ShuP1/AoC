import sys

paper = 0
ribbon = 0
for line in sys.stdin.readlines():
    a, b, c = sorted(map(int, line.split('x')))
    paper += 2*(a*b + b*c + c*a) + a*b
    ribbon += 2*(a+b) + a*b*c

print(paper)
print(ribbon)
