iday = input().split()
iday = int(iday[1])
iclock = input().split()
ihour = int(iclock[0])
iminute = int(iclock[2])
isecond = int(iclock[4])
fday = input().split()
fday = int(fday[1])
fclock = input().split()
fhour = int(fclock[0])
fminute = int(fclock[2])
fsecond = int(fclock[4])
d = fday - iday
h = fhour - ihour
if h < 0:
    h += 24
    if d != 0:
        d -= 1
m = fminute - iminute
if m < 0:
    m += 60
    if h != 0:
        h -= 1
    elif h == 0 and d != 0:
        d -= 1
        h = 23
s = fsecond - isecond
if s < 0:
    s += 60
    if m != 0:
        m -= 1
    elif m == 0 and h != 0:
        h = 23
    elif m == 0 and h == 0 and d != 0:
        d -= 1
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(d, h, m, s))
