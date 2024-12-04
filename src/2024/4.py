import sys

B = [l.strip() for l in sys.stdin]
X, Y = len(B), len(B[0])

def is_word(x, y, dx, dy, word):
    n = len(word) - 1
    return 0 <= x + dx * n < X and 0 <= y + dy * n < Y and \
        all(B[x + dx * i][y + dy * i] == word[i] for i in range(n+1))

print(sum(is_word(x, y, dx, dy, 'XMAS')
          for x in range(X) for y in range(Y)
          for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy))

def is_xmas(x, y):
    return (is_word(x - 1, y - 1, 1, 1, 'MAS') or is_word(x - 1, y - 1, 1, 1, 'SAM')) and (
            is_word(x + 1, y - 1, -1, 1, 'MAS') or is_word(x + 1, y - 1, -1, 1, 'SAM'))

print(sum(is_xmas(x, y) for x in range(X) for y in range(Y)))
