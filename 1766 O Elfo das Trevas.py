def menor(lista, x):
    ready = False
    while not ready:
        mud = 0
        for a in range(len(lista)):
            if a != len(lista) - 1 and float(lista[a][x]) > float(lista[a + 1][x]):
                mud = 1
                k = lista[a]
                lista[a] = lista[a + 1]
                lista[a + 1] = k
        if mud == 0:
            ready = True
def maior(lista, x):
    ready = False
    while not ready:
        mud = 0
        for a in range(len(lista)):
            if a != len(lista) - 1 and float(lista[a][x]) < float(lista[a + 1][x]):
                mud = 1
                k = lista[a]
                lista[a] = lista[a + 1]
                lista[a + 1] = k
        if mud == 0:
            ready = True
t = int(input())
for testes in range(t):
    n, m = [int(x) for x in input().split()]
    renas = []
    for rena in range(n):
        renas.append(input().split())
    renas.sort()
    menor(renas, 3)
    menor(renas, 2)
    maior(renas, 1)
    print('CENARIO {%d}' %(testes + 1))
    for p in range(m):
        print('{} - {}'.format(p + 1, renas[p][0]))
