import sys
import itertools

vals = [int(line) for line in sys.stdin.readlines()]

buffer = 25
invalid = next(vals[i] for i in range(buffer, len(vals)) if not any(a + b == vals[i] for a, b in itertools.combinations(vals[i - buffer: i], 2)))

print(invalid)

parts = (vals[i: i + r] for r in range(2, len(vals)) for i in range(len(vals) - r + 1))
print(next(min(part) + max(part) for part in parts if sum(part) == invalid))
