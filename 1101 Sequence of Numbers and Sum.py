som = 0
lista = []
while True:
    vv = input().split()
    v1 = int(vv[0])
    v2 = int(vv[1])
    if v1 <= 0 or v2 <= 0:
        break
    if v2 > v1:
        v1 = int(vv[1])
        v2 = int(vv[0])
    for c in range(v2, v1 + 1):
        lista.append(c)
        som += c
    lista.append('Sum={}'.format(som))
    som = 0
for b in lista:
    if str(b).isnumeric():
        print(b, '', end='')
    else:
        print(b)
