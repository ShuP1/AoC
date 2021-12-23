import sys
from heapq import heappop, heappush

lines = sys.stdin.readlines()
MAP = [''.join(lines[y][x] for y in range(2, 4)) for x in range(3, 10, 2)]

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, '.': 0}
TARGET = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

def is_free(path):
    return all(c == '.' for c in path)
def moves(size, state):
    hall = state[0]
    for h in [0, 1, 3, 5, 7, 9, 10]:
        if hall[h] == '.':
            for i, door in enumerate(range(2, 9, 2), 1):
                if state[i] and is_free(hall[h:door] if h < door else hall[door+1:h+1]):
                    amph = state[i][0]
                    ncost = COST[amph] * (1 + size - len(state[i]) + abs(h-door))
                    nstate = list(state)
                    nstate[i] = state[i][1:]
                    nstate[0] = hall[0:h] + amph + hall[h+1:]
                    yield tuple(nstate), ncost
        else:
            amph = hall[h]
            room = TARGET[amph]
            door = room * 2
            if len(state[room]) >= size or any(map(lambda a: a != amph, state[room])) \
            or not is_free(hall[h+1:door+1] if h < door else hall[door:h]):
                continue
            ncost = COST[amph] * (size - len(state[room]) + abs(h-door))
            nstate = list(state)
            nstate[0] = hall[0:h] + '.' + hall[h + 1 :]
            nstate[room] += amph
            yield tuple(nstate), ncost


def solve(size, start):
    close = {}
    GOAL = ('...........', *(chr(ord('A')+i)*size for i in range(4)))
    queue = [(0, ('...........', *start))]
    while queue:
        cost, state = heappop(queue)
        if state == GOAL:
            return cost
        for nstate, ncost in moves(size, state):
            ncost += cost
            if nstate not in close or close[nstate] > ncost:
                heappush(queue, (ncost, nstate))
                close[nstate] = ncost

print(solve(2, MAP))
P2 = ['DD', 'CB', 'BA', 'AC']
goal = (a[0] + b + a[1] for a, b in zip(MAP, P2))
print(solve(4, goal))
