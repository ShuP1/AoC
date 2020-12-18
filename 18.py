import sys
import re

def eval(line: str) -> str:
    def simplify(part: str) -> str:
        """
        while '+' in part or '*' in part:
            part = re.sub('^(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), part)
            part = re.sub('^(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), part)
        """
        # part 2:
        while '+' in part:
            part = re.sub('(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), part)
        while '*' in part:
            part = re.sub('(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), part)
        return part
    while '(' in line:
        line = re.sub(r'\(([^()]+)\)', lambda m: simplify(m.group(1)), line)
    return simplify(line)

print(sum(int(eval(l.strip())) for l in sys.stdin))