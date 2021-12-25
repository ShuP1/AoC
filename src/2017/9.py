import sys

LINE = sys.stdin.readline().strip()

def clear(line):
    trash = 0
    clean = ''
    i, I = 0, len(line)
    while i < I:
        if line[i] == '<':
            i += 1
            while LINE[i] != '>':
                if LINE[i] == "!":
                    i += 1
                else:
                    trash += 1
                i += 1
        else:
            clean += line[i]
        i += 1
    return clean, trash

content, trash = clear(LINE)
score, brackets = 0, 0
for c in content:
    if c == '{':
        brackets += 1
    elif c == '}':
        score += brackets
        brackets -= 1
print(score)
print(trash)
