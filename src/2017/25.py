import sys

lines = [line.strip().strip(':.- ').split() for line in sys.stdin.readlines()]
STEPS = int(lines[1][5])

RULES = dict()
for i in range(3, len(lines), 10):
    s = lines[i][2]
    do = []
    for j in range(0, 5, 4):
        w = int(lines[i+j+2][3])
        m = 1 if lines[i+j+3][5] == 'right' else -1
        c = lines[i+j+4][3]
        do.append((w, m, c))
    RULES[s] = tuple(do)

state = lines[0][3]
tape = set()
i = 0
for _ in range(STEPS):
    write, move, state = RULES[state][int(i in tape)]
    if write:
        tape.add(i)
    else:
        tape.discard(i)
    i += move
print(len(tape))
