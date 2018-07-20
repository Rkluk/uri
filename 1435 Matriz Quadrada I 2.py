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
    for c in range(user):
        for v in range(user):
            if c == v and c < (user // 2):
                matriz[c][v] = c + 1
            elif c == v and c >= (user // 2):
                matriz[c][v] = user - c
    for c in range(user):
        for v in range(user):
            matriz
                
    print(matriz)
