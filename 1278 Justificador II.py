g = 0
while True:
    n = int(input())
    if n == 0:
        break
    lista = []
    for c in range(n):
        lista.append(input().strip())
    l2 = []
    for c in lista:
        k = ''
        for v in range(len(c)):
            if c[v] == ' ' and c[v - 1] != ' ':
                k += c[v]
            elif c[v] != ' ':
                k += c[v]
        l2.append(k)
    h = ''
    for c in l2:
        if h == '' or len(c) > h:
            h = len(c)
    if g == 1:
        print('')
    for c in l2:
        print('{:>{}}'.format(c, h))
    g = 1
