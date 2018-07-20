while True:
    u = int(input())
    if u == 0:
        break
    m = []
    for c in range(u):
        lista = []
        for v in range(u):
            lista.append(1)
        m.append(lista)
    for c in range(u):
        for v in range(u):
            if c == v == 0:
                m[c][v] = 2 ** c
            elif c == v:
                m[c][v] = 2 ** (c * 2)
            else:
                m[c][v] = 2 ** (v + c)
    esp = len(str(m[u - 1][u - 1]))
    for c in range(u):
        for v in range(u):
            if v == u - 1:
                print('{:{}}'.format(m[c][v], esp))
            else:
                print('{:{}}'.format(m[c][v], esp), end=' ')
    print('')
