import sys, os
from itertools import count
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ocr import ocr_array

lines = sys.stdin.readlines()

i, w, x = 0, False, 1
signal = 0
screen = [['.'] * 40 for _ in range(6)]
for cycle in count(1):
    if i >= len(lines):
        break
    # during
    if (cycle+20)%40 == 0:
        signal += cycle*x
    px = (cycle-1)%40
    if abs(x-px)<=1:
        screen[(cycle-1)//40][px] = '#'
    # end
    op, *arg = lines[i].split()
    if op == 'noop':
        i += 1
    else: # addx
        if w:
            x += int(arg[0])
            i += 1
        w = not w

print(signal)
print(ocr_array(screen))
