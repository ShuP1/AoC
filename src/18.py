import sys
import re

def solve(line, p1):
    def simplify(part):
        if p1:
            while '+' in part or '*' in part:
                part = re.sub('^(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), part)
                part = re.sub('^(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), part)
        else:
            while '+' in part:
                part = re.sub('(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), part)
            while '*' in part:
                part = re.sub('(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), part)
        return part
    while '(' in line:
        line = re.sub(r'\(([^()]+)\)', lambda m: simplify(m.group(1)), line)
    return simplify(line)

lines = sys.stdin.readlines()
print(sum(int(solve(l.strip(), True)) for l in lines))
print(sum(int(solve(l.strip(), False)) for l in lines))