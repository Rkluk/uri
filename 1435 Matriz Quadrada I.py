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
    if user % 2 == 0:
        for c in range(user):
            for b in range(user):
                if c != 0 and c != user - 1 and b != 0 and b != user - 1:
                    if b <= (user / 2):
                        matriz[c][b] = matriz[c - 1][b] + matriz[c][b - 1]
                    else:
                        matriz[c - 1][b] + matriz[c][b + 1]
                else:
                    matriz[c][b] = 1
    else:
        for c in range(user):
            for b in range(user):
                if c != 0 and c != user -1 and b != 0 and b != user - 1:
                    if b <= ((user // 2) + 1) and c <= ((user // 2) + 1):
                        matriz[c][b] = matriz[c - 1][b] + matriz[c][b - 1]
                    elif b <= ((user // 2) + 1):
                        matriz[c][b] = matriz[c - 1][b] + matriz[c][b - 1]
                    else:
                        matriz[c - 1][b] + matriz[c][b + 1]
                else:
                    matriz[c][b] = 1
    print(matriz)
                
