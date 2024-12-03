import sys
import re

B = '\n'.join(sys.stdin)

ins = re.findall(r"(?:do(n't)?\(\))|(?:mul\((\d{1,3}),(\d{1,3})\))", B)
mul = lambda ins: sum(int(a) * int(b) for _,a,b in ins if a)
print(mul(ins))

on = True
def on_off(t):
    global on
    nt,a,_ = t
    if not a:
        on = not nt
    return on
print(mul(filter(on_off, ins)))
