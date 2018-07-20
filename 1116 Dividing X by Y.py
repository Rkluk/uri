user = int(input())
lista = []
for z in range(0, user):
    x, y = [int(c) for c in input().split()]
    if y == 0:
        lista.append('divisao impossivel')
    else:
        v = x / y
        v = round(v, 1)
        lista.append(v)
for m in lista:
    print(m)
