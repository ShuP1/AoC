import sys

cubes = {tuple(map(int, l.split(','))) for l in sys.stdin.readlines()}

def adjs(x, y, z):
    for dx,dy,dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        yield x+dx,y+dy,z+dz
def area(subset):
    return sum(face not in subset for cube in subset for face in adjs(*cube))

N = area(cubes)
print(N)

air = {
    (x,y,z)
    for x in range(min(x for x,_,_ in cubes)-1, max(x for x,_,_ in cubes)+2)
    for y in range(min(y for _,y,_ in cubes)-1, max(y for _,y,_ in cubes)+2)
    for z in range(min(z for _,_,z in cubes)-1, max(z for _,_,z in cubes)+2)
    if (x,y,z) not in cubes
}
q = [min(air)]
while q:
    pt = q.pop()
    if pt in air:
        air.remove(pt)
        for cpt in adjs(*pt):
            q.append(cpt)
print(N-area(air))
