import sys

R, P = sys.stdin.read().split('\n\n')
R = [int(l.split()[-1]) for l in R.splitlines()]
P = list(map(int, P.split()[1].split(',')))

def run(a, b=0, c=0, debug=None):
    i = 0
    while i < len(P):
        op, v = P[i], P[i+1]
        i += 2
        combo = v
        match v:
            case 4: combo = a
            case 5: combo = b
            case 6: combo = c
        match op:
            case 0: a //= 2**combo
            case 1: b ^= v
            case 2: b = combo % 8
            case 3: i = v if a else i
            case 4: b ^= c
            case 5:
                w = combo % 8
                if not debug:
                    return w
                debug(w)
            case 6: b = a // 2**combo
            case 7: c = a // 2**combo

out = []
run(*R, out.append)
print(','.join(map(str, out)))

def solve(n, prev):
    if n < 0:
        return prev
    for mask in range(8):
        a = prev * 8 | mask
        if run(a) == P[n]:
            if win := solve(n-1, a):
                return win
print(solve(len(P)-1, 0))
