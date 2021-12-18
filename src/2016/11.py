import sys
from re import compile
from itertools import chain, combinations
from collections import deque, Counter

def is_valid_transition(floor):
    return len(set(type for _, type in floor)) < 2 or all((obj, 'generator') in floor for (obj, type) in floor if type == 'microchip')


def next_states(state):
    moves, elevator, floors = state

    possible_moves = chain(combinations(
        floors[elevator], 2), combinations(floors[elevator], 1))

    for move in possible_moves:
        for direction in [-1, 1]:
            next_elevator = elevator + direction
            if not 0 <= next_elevator < len(floors):
                continue

            next_floors = floors.copy()
            next_floors[elevator] = next_floors[elevator].difference(move)
            next_floors[next_elevator] = next_floors[next_elevator].union(move)

            if (is_valid_transition(next_floors[elevator]) and is_valid_transition(next_floors[next_elevator])):
                yield (moves + 1, next_elevator, next_floors)


def uuid(state):
    _, elevator, floors = state
    return elevator, tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in floors)

def solve(floors):
    TOP_FLOOR = len(floors) - 1
    close = set()
    queue = deque([(0, 0, floors)])
    while queue:
        state = queue.popleft()
        moves, _, floors = state

        if not any(i < TOP_FLOOR and floor for i, floor in enumerate(floors)):
            return moves # done

        for next_state in next_states(state):
            key = uuid(next_state)
            if (key) not in close:
                close.add(key)
                queue.append(next_state)

RE = compile(r'(\w+)(?:-compatible)? (microchip|generator)')
floors = [set(RE.findall(line)) for line in sys.stdin.readlines()]

print(solve(floors))

floors[0] = floors[0].union([
    ('elerium', 'generator'), ('elerium', 'microchip'),
    ('dilithium', 'generator'), ('dilithium', 'microchip')
])
print(solve(floors))
