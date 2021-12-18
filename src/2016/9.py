import sys

line = sys.stdin.readline().strip()

def run(s, rec=False):
    l = 0
    while True:
        start = s.find('(')
        end = s.find(')', start)
        if end >= 0:
            sl, n = map(int, s[start+1:end].split('x'))
            l += start
            s = s[end+1:]
            l += (run(s[:sl], True) if rec else sl) * n
            s = s[sl:]
        else:
            l += len(s)
            break
    return l

print(run(line, False))
print(run(line, True))
