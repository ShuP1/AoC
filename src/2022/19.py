import sys,re
from math import prod

blues = [tuple(map(int, re.findall(r'\d+', line))) for line in sys.stdin.readlines()]

def sim(blue, time):
    _, oreore, claore, obsore, obscla, geoore, geoobs = blue
    maxore = max(oreore, claore, obsore, geoore)
    def rec(time, bore, bcla, bobs, bgeo, ore, cla, obs, geo):
        if geo + bgeo*time + (time-1) * time//2 <= rec.mx:
            return
        if bore < maxore:
            t = max(0, -((ore-oreore)//bore))+1
            if time >= t:
                rec(time-t, bore+1, bcla, bobs, bgeo, ore-oreore+bore*t, cla+bcla*t, obs+bobs*t, geo+bgeo*t)
        if bcla < obscla:
            t = max(0, -((ore-claore)//bore))+1
            if time >= t:
                rec(time-t, bore, bcla+1, bobs, bgeo, ore-claore+bore*t, cla+bcla*t, obs+bobs*t, geo+bgeo*t)
        if bobs < geoobs and bcla:
            t = max(0, -((ore-obsore)//bore), -((cla-obscla)//bcla))+1
            if time >= t:
                rec(time-t, bore, bcla, bobs+1, bgeo, ore-obsore+bore*t, cla-obscla+bcla*t, obs+bobs*t, geo+bgeo*t)
        if bobs:
            t = max(0, -((ore-geoore)//bore), -((obs-geoobs)//bobs))+1
            if time >= t:
                rec(time-t, bore, bcla, bobs, bgeo+1, ore-geoore+bore*t, cla+bcla*t, obs-geoobs+bobs*t, geo+bgeo*t)
        rec.mx = max(rec.mx, geo)
        return rec.mx
    rec.mx = 0
    return rec(time, 1, 0, 0, 0, 0, 0, 0, 0)

print(sum(blue[0]*sim(blue, 24) for blue in blues))
print(prod(sim(blue, 32) for blue in blues[:3]))
