from math import log2
from math import floor
while True:
    c = int(input())
    if c == 0:
        break
    pui, pri, pii = [0, 0, 0]
    for game in range(c):
        ui, ri, ii = [int(x) for x in input().split()]
        k = [int(ui), int(ri), int(ii)]
        k.sort()
        if ui % 2 == 0:
            lui = log2(ui)
            if lui - floor(lui) == 0:
                pui += 1
                if ui == k[2]:
                    pui += 1
        if ri % 2 == 0:
            lri = log2(ri)
            if lri - floor(lri) == 0:
                pri += 1
                if ri == k[2]:
                    pri += 1
        if ii % 2 == 0:
            lii = log2(ii)
            if lii - floor(lii) == 0:
                pii += 1
                if ii == k[2]:
                    pii += 1
    points = [int(pui), int(pri), int(pii)]
    points.sort()
    if points[2] == points[1]:
        print('URI')
    elif pri > pui and pri > pii:
        print('Rita')
    elif pui > pri and pui > pii:
        print('Uilton')
    elif pii > pui and pii > pri:
        print('Ingred')
