p1 = 0
p2 = 19
lista = []
for c in range(20):
    user = int(input())
    lista.append(user)
for v in range(10):
    x = lista[p1]
    y = lista[p2]
    lista[p1] = y
    lista[p2] = x
    p1 += 1
    p2 -= 1
for b in range(len(lista)):
    print('N[{}] = {}'.format(b, lista[b]))
