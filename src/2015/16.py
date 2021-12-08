import sys

MFCSAM = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

lines = sys.stdin.readlines()

def scan(where):
    for line in lines:
        sue, rest = line.strip().split(': ', 1)
        for dna in rest.split(', '):
            k, v = dna.split(': ')
            if k in MFCSAM and where(k, int(v)):
                break
        else:
            return sue[4:]

print(scan(lambda k, v: MFCSAM[k] != v))

def v2(k, v):
    if k in ['cats', 'trees']:
        return v <= MFCSAM[k]
    if k in ['pomeranians', 'goldfish']:
        return v >= MFCSAM[k]
    return MFCSAM[k] != int(v)

print(scan(v2))
