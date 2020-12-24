import sys
import itertools

line = sys.stdin.readline().strip()

def exec(code, a = None, b = None):
    if a is not None:
        code[1] = a
    if b is not None:
        code[2] = b

    i = 0
    while i < len(code):
        if code[i] == 1:
            code[code[i+3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] == 2:
            code[code[i+3]] = code[code[i + 1]] * code[code[i + 2]]
        elif code[i] == 99:
            break

        i += 4
    return code[0]

print(exec(list(map(int, line.split(','))), 12, 2))

target = 19690720
for a, b in itertools.combinations_with_replacement(range(99 + 1), 2):
    if exec(list(map(int, line.split(','))), a, b) == target:
        print(100 * a + b)
        break