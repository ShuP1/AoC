import sys

pwd = list(sys.stdin.readline().strip())

JMP = 'hnk' # 'iol'-1
def inc(pwd):
    for i in reversed(range(len(pwd))):
        pwd[i] = chr(ord(pwd[i]) + 1 + int(pwd[i] in JMP))
        if pwd[i] <= 'z':
            break
        pwd[i] = 'a'

def double(line):
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            return i
    else:
        return None

def valid(pwd):
    if not any([ord(a)+1 == ord(b) == ord(c)-1 for a, b,c in zip(pwd[:-2], pwd[1:-1], pwd[2:])]):
        return False
    
    i = double(pwd)
    return not (i is None or double(pwd[i+2:]) is None)

def next(pwd):
    while not valid(pwd):
        inc(pwd)
    print(''.join(pwd))

next(pwd)
inc(pwd)
next(pwd)
