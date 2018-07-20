results = []
while True:
    x, y = [int(x) for x in input().split()]
    k = 0
    if (x and y) == 0:
        break
    lista = list(str(y))
    lista2 = list(str(y))
    x = str(x)
    for v in range(0, len(lista)):
        if x == lista[v]:
            del lista2[v - k]
            k += 1
    if lista2 == []:
        lista2.append('0')
    results.append(int(''.join(lista2)))
for c in results:
    print(c)
