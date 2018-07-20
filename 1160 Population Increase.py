lista = []
t = int(input())
for c in range(t):
    pa, pb, g1, g2 = [float(x) for x in input().split()]
    pa = int(pa)
    pb = int(pb)
    count = 0
    while not(pa > pb) and count <= 100:
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        count += 1
    if count <= 100:
        lista.append('{} anos.'.format(count))
    else:
        lista.append('Mais de 1 seculo.')
for v in lista:
    print(v)
