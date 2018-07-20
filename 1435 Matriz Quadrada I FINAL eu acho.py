while True:
    user = int(input())
    if user == 0:
        break
    matriz = []
    v = 0
    for c in range(user):
        linha = []
        for v in range(user):
                linha.append(1)
        matriz.append(linha)
    val = 1
    rig = user - 1
    lef = 0
    up = 0
    down = user - 1
    mid = user / 2 if user % 2 == 0 else (user + 1) / 2
    while val <= mid:
        for c in range(lef, rig + 1):
            matriz[c][lef] = val
            matriz[c][rig] = val
        for c in range(up, down + 1):
            matriz[up][c] = val
            matriz[down][c] = val
        val += 1
        rig -= 1
        lef += 1
        up += 1
        down -= 1
    for c in range(user):
        for v in range(user):
            if v == user - 1:
                print('{:3}'.format(matriz[c][v]))
            else:
                print('{:3}'.format(matriz[c][v]), end=' ')
    print('')
