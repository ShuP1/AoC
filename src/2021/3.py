import sys
from functools import reduce

lines = [line.strip() for line in sys.stdin.readlines()]
LEN = len(lines[0])

g = [sum([line[i] == '1' for line in lines]) > len(lines) / 2 for i in range(LEN)]
def g2i(invert):
    return int(''.join(map(lambda c: '1' if c ^ invert else '0', g)), 2)

print(g2i(False) * g2i(True))

def criterion(invert):
    def critera(lines, i):
        if len(lines) > 1:
            prefer = '1' if sum([line[i] == '0' for line in lines]) > len(lines) / 2 else '0'
            return [line for line in lines if (line[i] == prefer) ^ invert]
        else:
            return lines

    return int(reduce(critera, range(LEN), lines)[0], 2)

print(criterion(False) * criterion(True))