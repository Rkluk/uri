while True:
    try:
        u = int(input())
        m = []
        for c in range(u):
            lista = []
            for v in range(u):
                lista.append(3)
            m.append(lista)
        for c in range(u):
            for v in range(u):
                if (u - (c + 1)) == v:
                    m[c][v] = 2
                elif c == v:
                    m[c][v] = 1
        for c in range(u):
            for v in range(u):
                if v == u - 1:
                    print('{}'.format(m[c][v]))
                else:
                    print('{}'.format(m[c][v]), end='')
    except EOFError:
        break
