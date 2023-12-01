import sys

lines = sys.stdin.readlines()
def solve(digit):
    return sum(int(
        next(digit(line, i) for i in range(len(line)) if digit(line, i)) +
        next(digit(line, i) for i in reversed(range(len(line))) if digit(line, i))
    ) for line in lines)

print(solve(lambda line, i: line[i].isnumeric() and line[i]))

NUMS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
        "six": 6, "seven": 7, "eight": 8, "nine": 9}
print(solve(lambda line, i: line[i].isnumeric() and line[i] or
            next((str(num) for word, num in NUMS.items() if line.startswith(word, i)), False)))
