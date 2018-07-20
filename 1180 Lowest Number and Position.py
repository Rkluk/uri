user = int(input())
lista = []
lista.append([int(x) for x in input().split()])
b = ''
for c in range(user):
    if b == '' or lista[0][c] < b:
        posicao = c
        b = lista[0][c]
print('Menor valor: {}\nPosicao: {}'.format(b, posicao))
