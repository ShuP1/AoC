import sys
import functools

inp = [int(i) for i in sys.stdin.readline().strip()]

def wrap(lst, i):
    return i%len(lst)

def wrap_slice(lst, start, count):
    return [lst[wrap(lst, i)] for i in range(start, start+count)]

# part 1
minus = min(inp)
maxim = max(inp)
def step(cups):
    pick = wrap_slice(cups, 1, 3)
    others = wrap_slice(cups, 4, len(cups) - 3)
    dest_i = None
    dest = cups[0]-1
    while dest_i is None:
        if dest in others:
            dest_i = others.index(dest)
        else:
            dest -= 1
            if dest < minus:
                dest = maxim

    return others[:dest_i+1] + pick + others[dest_i+1:]

cups = [i for i in inp]
for _ in range(100):
    cups = step(cups)

print(''.join(str(i) for i in wrap_slice(cups, cups.index(1) + 1, len(cups) - 1)))

# part 2
cups = [i for i in inp] + list(range(max(inp) + 1, 1000000 + 1))

class LinkedNode:
    __slots__ = ('value', 'next')

    def __init__(self, value):
        self.value = value
        self.next = None

def solve(cups, N):
    lst = {i: LinkedNode(i) for i in cups}
    for a, b in zip(cups, cups[1:] + cups[:1]):
        lst[a].next = lst[b]

    front = lst[cups[0]]
    for n in range(N):
        a = front.next
        b = a.next
        c = b.next
        pick = set([a.value, b.value, c.value])

        dest = front.value
        while True:
            dest -= 1
            if dest == 0:
                dest = len(cups)
            if dest not in pick:
                break

        d = lst[dest]
        front.next, front, d.next, c.next = c.next, c.next, a, d.next

    a = lst[1].next
    return a.value * a.next.value

print(solve(cups, 10000000))