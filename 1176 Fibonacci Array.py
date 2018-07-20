user = int(input())
lista = []
m = 0
n = 0
for c in range(0, 61):
    lista.append(m)
    if m == 0:
        m += 1
    else:
        m += n
        n = j
    j = m
lista2 = []
for x in range(user):
    num = int(input())
    lista2.append('Fib({}) = {}'.format(num, lista[num]))
for f in lista2:
    print(f)
