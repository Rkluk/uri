n = int(input())
letras = []
letras.append([chr(x) for x in range(97, 123)])
letras = letras[0]
for c in range(n):
    frase = input()
    cont = 0
    for x in letras:
        if x in frase:
            cont += 1
    if cont == 26:
        print('frase completa')
    elif cont >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
