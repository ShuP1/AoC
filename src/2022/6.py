import sys

packet = sys.stdin.readline()
def start_of(n): 
    return next(i for i in range(n, len(packet))
        if len(set(packet[i-n:i])) == n)

print(start_of(4))
print(start_of(14))
