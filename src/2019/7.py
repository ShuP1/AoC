import sys
import itertools

line = sys.stdin.readline().strip()

class Intcode:
    __slots__ = ('i', 'code', 'inps')

    def __init__(self, line, inps = []):
        self.i = 0
        self.code = list(map(int, line.split(',')))
        self.inps = inps

    def write(self, i, m, v):
        j = i if m else self.code[i]
        self.code[j] = v

    def get(self, i, m):
        return self.code[i] if m else self.code[self.code[i]]

    def push(self, inp):
        self.inps.append(inp)

    def pull(self):
        while self.i < len(self.code):
            op = self.code[self.i] % 100
            m1 = self.code[self.i] // 100 % 10 == 1
            m2 = self.code[self.i] // 1000 % 10 == 1
            m3 = self.code[self.i] // 10000 % 10 == 1

            if op == 1:
                self.write(self.i+3, m3, self.get(self.i+1, m1) + self.get(self.i+2, m2))
                self.i += 4
            elif op == 2:
                self.write(self.i+3, m3, self.get(self.i+1, m1) * self.get(self.i+2, m2))
                self.i += 4
            elif op == 3:
                self.write(self.i+1, m1, self.inps.pop(0))
                self.i += 2
            elif op == 4:
                self.i += 2
                return self.get(self.i+1-2, m1)
            elif op == 5:
                if self.get(self.i+1, m1) != 0:
                    self.i = self.get(self.i+2, m2)
                else:
                    self.i += 3
            elif op == 6:
                if self.get(self.i+1, m1) == 0:
                    self.i = self.get(self.i+2, m2)
                else:
                    self.i += 3
            elif op == 7:
                self.write(self.i+3, m3, 1 if self.get(self.i+1, m1) < self.get(self.i+2, m2) else 0)
                self.i += 4
            elif op == 8:
                self.write(self.i+3, m3, 1 if self.get(self.i+1, m1) == self.get(self.i+2, m2) else 0)
                self.i += 4
            elif op == 99:
                break

    def process(self, inp):
        self.push(inp)
        return self.pull()

max_th = -1
for phs in itertools.permutations(range(5), 5):
    inp = 0
    for ph in phs:
        amp = Intcode(line, [ph])
        inp = amp.process(inp)
    if inp > max_th:
        max_th = inp

print(max_th)

max_th = -1
for phs in itertools.permutations(range(5, 10), 5):
    amps = [Intcode(line, [ph]) for ph in phs]

    inp = 0
    running = True
    while running:
        for amp in amps:
            res = amp.process(inp)
            if res is None:
                running = False
                break

            inp = res

    if inp > max_th:
        max_th = inp

print(max_th)