import sys

ops = dict()
vals = dict()
def eval(part):
    if not (part in vals):
        vals[part] = int(part) if part.isdigit() else ops[part]()
    return vals[part]

def to_op(ins):
    parts = ins.split(' ')
    l = len(parts)
    if l == 1:
        return lambda: eval(parts[0])
    elif l == 2:
        return lambda: ~eval(parts[1])
    else: # l == 3
        if parts[1] == 'AND':
            return lambda: eval(parts[0]) & eval(parts[2])
        elif parts[1] == 'OR':
            return lambda: eval(parts[0]) | eval(parts[2])
        elif parts[1] == 'LSHIFT':
            return lambda: eval(parts[0]) << eval(parts[2])
        elif parts[1] == 'RSHIFT':
            return lambda: eval(parts[0]) >> eval(parts[2])
        else:
            print(ins, file=sys.stderr)

for line in sys.stdin.readlines():
    ins, wire = line.strip().split(' -> ')
    ops[wire] = to_op(ins)

a = eval('a')
print(a)
vals.clear()
vals['b'] = a
print(eval('a'))
