lista = []
while True:
    vv = input().split()
    v1 = int(vv[0])
    v2 = int(vv[1])
    if v1 == v2:
        break
    elif v1 > v2:
        lista.append('Decrescente')
    elif v1 < v2:
        lista.append('Crescente')
for b in lista:
    print(b)
