import sys

DISK = {}

pwd = []
for line in sys.stdin.readlines():
    line = line.strip()
    if line[:4] == '$ cd':
        arg = line[5:]
        if arg == "/":
            pwd.clear()
        elif arg == "..":
            pwd.pop()
        else:
            pwd.append(arg)
    elif line == '$ ls':
        pass
    else: # in ls
        t,name = line.split()
        if t != 'dir':
            d = DISK
            for p in pwd:
                if p not in d:
                    d[p] = {}
                d = d[p]
            d[name] = int(t)

def reduce_sizes(d, fn, acc=0):
    s = 0
    for v in d.values():
        if type(v) is int:
            s += v
        else:
            t, acc = reduce_sizes(v, fn, acc)
            s += t
    return s, fn(acc, s)

TOTAL,P1=reduce_sizes(DISK, lambda acc,s: acc+int(s <= 100000)*s)
print(P1)

TO_FREE=TOTAL+30000000-70000000
_,P2=reduce_sizes(DISK, lambda acc,s: s if s >= TO_FREE and s < acc else acc, TOTAL)
print(P2)
