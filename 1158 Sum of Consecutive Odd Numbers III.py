user = int(input())
lista = []
for c in range(user):
    x, y = [int(v) for v in input().split()]
    if x % 2 == 1:
        soma = x
        for b in range(1, y):
            soma += x + (2 * b)
        lista.append(soma)
    else:
        soma = x + 1
        x += 1
        for b in range(1, y):
            soma += x + (2 * b)
        lista.append(soma)
for c in lista:
    print(c)
