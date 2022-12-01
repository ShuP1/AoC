import sys

elfs = '\t'.join(sys.stdin.readlines()).split('\t\n')
elfs = [sum(int(c) for c in elf.splitlines()) for elf in elfs]
elfs.sort(reverse=True)

print(elfs[0])
print(sum(elfs[0:3]))
