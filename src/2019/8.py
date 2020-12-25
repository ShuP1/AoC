import sys

X = 25
x = 0
Y = 6
y = 0
layers = []
for char in sys.stdin.readline().strip():
    if x == 0:
        if y == 0:
            layers.append([])
        layers[-1].append('')

    layers[-1][-1] += char
    x += 1
    if x >= X:
        x = 0
        y += 1
        if y >= Y:
            y = 0

nb_z = X * Y
res = None
for layer in layers:
    nb = sum(line.count('0') for line in layer)
    if nb < nb_z:
        nb_z = nb
        res = sum(line.count('1') for line in layer) * sum(line.count('2') for line in layer)

print(res)

image = []
for y in range(Y):
    image.append('')
    for x in range(X):
        for i in range(len(layers)):
            v = layers[i][y][x]
            if v != '2':
                image[-1] += ('#' if v == '0' else ' ')
                break

# README: print('\n'.join(image))
print('LGYHB')