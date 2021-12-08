import sys

line = sys.stdin.readline().strip()

def step(line):
    out = ''
    t = 1
    v = line[0]
    for c in line[1:] + 'x':
        if c == v:
            t += 1
        else:
            out += str(t) + v
            t = 1
            v = c
    return out

def run(n):
    global line
    for _ in range(n):
        line = step(line)
    print(len(line))

run(40)
run(50-40)
