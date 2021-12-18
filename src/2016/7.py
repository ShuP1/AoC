import sys

def abba(s):
    return any(s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]
        for i in range(len(s)-3))

def abas(s):
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i] == s[i+2]:
            yield s[i:i+3]
def bab(s, aba):
    a,b = aba[:2]
    return s.find(b+a+b) >= 0

def split(line):
    super = []
    hyper = []
    l = line
    while True:
        start = l.find('[')
        end = l.find(']', start)
        if end < 0:
            break
        super.append(l[:start])
        hyper.append(l[start+1:end])
        l = l[end+1:]
    super.append(l)
    return super, hyper

parts = [split(line.strip()) for line in sys.stdin.readlines()]

tls = sum(any(map(abba, super)) and not any(map(abba, hyper))
    for super, hyper in parts)
print(tls)

ssl = sum(any(bab(h, aba) for abas in map(abas, super) for aba in abas for h in hyper)
    for super, hyper in parts)
print(ssl)
