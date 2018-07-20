while True:
    user = int(input())
    if user == 0:
        break
    m = []
    for c in range(user):
        l = []
        for v in range(user):
            l.append(1)
        m.append(l)
    for c in range(user):
        m[c][0] = c + 1
        m[0][c] = c + 1
    k = 0
    for c in range(1, user):
        for v in range(1, user):
            if k == 0:
                m[c][v] = m[c][v - 1] - 1
            elif k == 1:
                m[c][v] = m[c][v - 1] + 1
            try:
                 if m[c][v] == 1:
                        k = 1
            except:
                k = 0
        k = 0
    for v in range(len(m)):
        for c in range(len(m)):
            if c == user - 1:
                print('{:3}'.format(m[v][c]))
            else:
                print('{:3}'.format(m[v][c]), end=' ')
    print('')

        
