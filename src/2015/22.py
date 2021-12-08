import sys

E_HITS, E_D = [int(line.split(': ')[1]) for line in sys.stdin.readlines()]
M_HITS, MANA = 50, 500

SPELLS = [
    # cost, dmg, heal, arm, mana, delay
    (53, 4, 0, 0, 0, 0),
    (73, 2, 2, 0, 0, 0),
    (113, 0, 0, 7, 0, 6),
    (173, 3, 0, 0, 0, 6),
    (229, 0, 0, 0, 101, 5)
]

def run(hard):
    min_cost = 1e30
    queue = [((E_HITS, M_HITS, MANA, [], True, 0))]
    while queue:
        e_h, m_h, mana, effects, m_turn, cost = queue.pop()

        if cost >= min_cost:
            continue

        if hard and m_turn:
            m_h -= 1
            if m_h <= 0:
                continue

        m_arm = 0
        for s, _ in effects:
            effect = SPELLS[s]
            e_h -= effect[1]
            m_h += effect[2]
            m_arm += effect[3]
            mana += effect[4]
        effects = [(s, d-1) for s, d in effects if d > 1]

        if e_h <= 0:
            min_cost = min(cost, min_cost)
            continue

        if m_turn:
            for s in range(len(SPELLS)):
                if any(map(lambda e: e[0] == s, effects)):
                    continue # already active

                spell_cost = SPELLS[s][0]
                if spell_cost > mana:
                    continue
                queue.append((e_h, m_h, mana - spell_cost, effects + [(s, SPELLS[s][5])], False, cost + spell_cost))
        else:
            m_h -= max(1, E_D - m_arm)
            if m_h > 0:
                queue.append((e_h, m_h, mana, effects, True, cost))

    return min_cost

print(run(False))
print(run(True))
