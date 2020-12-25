import sys
import itertools

card_pub = int(sys.stdin.readline())
door_pub = int(sys.stdin.readline())

def transform(subject, times):
    v = 1
    for _ in range(times):
        v *= subject
        v %= 20201227
    return v

def solve(subject, pub):
    v = 1
    for i in itertools.count():
        if v == pub:
            return i
        v *= subject
        v %= 20201227

card_times = solve(7, card_pub)
door_times = solve(7, door_pub)

enc = transform(door_pub, card_times)
assert enc == transform(card_pub, door_times)
print(enc)