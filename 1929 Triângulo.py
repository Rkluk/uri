a, b, c, d = [int(x) for x in input().split()]
lista = [a, b, c, d]
lista.sort()
if lista[3] - lista[2] < lista[1] < lista[3] + lista[2] or lista[2] - lista[1] < lista[0] < lista[2] + lista[1]:
    print('S')
else:
    print('N')
