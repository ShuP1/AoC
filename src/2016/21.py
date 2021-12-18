import sys
from itertools import permutations

lines = sys.stdin.readlines()

def apply(pwd):
    pwd = list(pwd)
    for line in lines:
        parts = line.strip().split()
        if parts[0] == 'swap':
            if parts[1] == 'position':
                ia, ib = int(parts[2]), int(parts[5])
                pwd[ia], pwd[ib] = pwd[ib], pwd[ia]
            else: # lettre
                a, b = parts[2], parts[5]
                pwd = [a if c == b else (b if c == a else c) for c in pwd]
        elif parts[0] == 'rotate':
            l = len(pwd)
            if parts[1] == 'based':
                n = pwd.index(parts[6])
                if n >= 4:
                    n += 1
                n += 1
            else:
                n = int(parts[2])
                if parts[1] == 'left':
                    n *= -1
            pwd = [pwd[(i-n)%l] for i in range(l)]
        elif parts[0] == 'reverse':
            ia, ib = int(parts[2]), int(parts[4])
            pwd = pwd[:ia] + (pwd[ib:ia-1:-1] if ia else pwd[ib::-1]) + pwd[ib+1:]
        else: # move
            ia, ib = int(parts[2]), int(parts[5])
            pwd.insert(ib, pwd.pop(ia))
    return ''.join(pwd)

print(apply('abcdefgh'))
for pwd in permutations('abcdefgh'):
    if apply(pwd) == 'fbgdceah':
        print(''.join(pwd))
        break
