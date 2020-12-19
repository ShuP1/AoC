import sys

rules = {}
line = sys.stdin.readline()
while line.strip():
    num, rest = line.strip().split(': ')
    rules[int(num)] = [[int(i) if i.isdigit() else i.strip('"') for i in option.split(' ')] for option in rest.split(' | ')]
    line = sys.stdin.readline()

# part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

messages = [line.strip() for line in sys.stdin.readlines()]

def is_valid(message):
    # [[rule, option, step], remaining]
    states = [[[(0, 0, 0)], message]]
    while states:
        new_states = []
        for state in states:
            st = state[0][-1]
            state[0].pop(-1)
            rule = rules[st[0]][st[1]][st[2]]
            if isinstance(rule, str):
                if state[1] and state[1][0] == rule:
                    state[1] = state[1][1:]
                    if len(state[0]):
                        new_states.append(state)
                    elif len(state[1]) == 0:
                        return True
            else:
                opts = rules[rule]
                if st[2]+1 < len(rules[st[0]][st[1]]):
                    state[0].append((st[0], st[1], st[2] + 1))
                for opt in range(len(opts)):
                    new_states.append([state[0] + [(rule, opt, 0)], state[1]])

        states = new_states

    return False


valids = 0
for message in messages:
    if is_valid(message):
        valids +=1

print(valids)