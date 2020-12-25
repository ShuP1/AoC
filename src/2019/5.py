import sys
import itertools

line = sys.stdin.readline().strip()

def exec(code, inp = None):
    outs = []
    i = 0
    while i < len(code):
        op = code[i] % 100
        m1 = code[i] // 100 % 10 == 1
        m2 = code[i] // 1000 % 10 == 1
        m3 = code[i] // 10000 % 10 == 1

        def sett(i, m, v):
            j = i if m else code[i]
            code[j] = v

        def get(i, m):
            return code[i] if m else code[code[i]]

        if op == 1:
            sett(i+3, m3, get(i+1, m1) + get(i+2, m2))
            i += 4
        elif op == 2:
            sett(i+3, m3, get(i+1, m1) * get(i+2, m2))
            i += 4
        elif op == 3:
            sett(i+1, m1, inp)
            i += 2
        elif op == 4:
            outs.append(get(i+1, m1))
            i += 2
        elif op == 5:
            if get(i+1, m1) != 0:
                i = get(i+2, m2)
            else:
                i += 3
        elif op == 6:
            if get(i+1, m1) == 0:
                i = get(i+2, m2)
            else:
                i += 3
        elif op == 7:
            sett(i+3, m3, 1 if get(i+1, m1) < get(i+2, m2) else 0)
            i += 4
        elif op == 8:
            sett(i+3, m3, 1 if get(i+1, m1) == get(i+2, m2) else 0)
            i += 4
        elif op == 99:
            break

    return outs

print(exec(list(map(int, line.split(','))), 1)[-1])
print(exec(list(map(int, line.split(','))), 5)[-1])
