import sys

groups = [l.strip() for l in sys.stdin.read().split('\n\n') if l.strip()]

desks = [[int(card.strip()) for card in part.split('\n')[1:] if card.strip()] for part in groups]

def game1(desks):
    while all(desks):
        a = desks[0].pop(0)
        b = desks[1].pop(0)
        if a > b:
            desks[0].append(a)
            desks[0].append(b)
        elif b > a:
            desks[1].append(b)
            desks[1].append(a)
        else:
            print("fail", a, b)
    return desks

def game2(desks):
    cache = set()
    while all(desks):
        key = tuple(tuple(desk) for desk in desks)
        if key in cache:
            return [[0], []] # player 1 wins
        else:
            cache.add(key)

        a = desks[0].pop(0)
        b = desks[1].pop(0)
        a_win = False
        b_win = False
        if len(desks[0]) >= a and len(desks[1]) >= b:
            if game2([[card for card in desks[0][:a]], [card for card in desks[1][:b]]])[0]:
                a_win = True
            else:
                b_win = True

        if a_win or ((not b_win) and a > b):
            desks[0].append(a)
            desks[0].append(b)
        elif b_win or b > a:
            desks[1].append(b)
            desks[1].append(a)
        else:
            print("fail", a, b)
    return desks

def score(desks):
    win = next(desk for desk in desks if desk)
    return sum((i + 1) * v for i, v in enumerate(reversed(win)))

part1 = game1([[card for card in desk] for desk in desks])
print(score(part1))

print(score(game2(desks)))