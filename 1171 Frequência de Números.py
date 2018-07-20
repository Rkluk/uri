dic, lista, mud = [{}, [], 1]
for c in range(int(input())):
    num = int(input())
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1
for c in dic:
    lista.append('{} aparece {} vez(es)'.format(c, dic[c]))
while mud == 1:
    mud = 0
    for c in range(len(lista) - 1):
        if int(lista[c][:lista[c].find(' ')]) > int(lista[c + 1][:lista[c + 1].find(' ')]):
            lista[c], lista[c + 1] = lista[c + 1], lista[c]
            mud = 1
for c in lista:
    print(c)
