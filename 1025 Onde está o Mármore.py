count = 1
while True:
    n, q = input().split()
    if n == '0' == q:
        break
    print('CASE# {}:'.format(count))
    lista = []
    consultas = []
    for c in range(int(n) + int(q)):
        if c < int(n):
            lista.append(int(input()))
        else:
            consultas.append(int(input()))
    lista = sorted(lista)
    for c in consultas:
        notfound = True
        first = 0
        last = len(lista) - 1
        while first <= last:
            middle = (first + last) // 2
            if c == lista[middle] and c != lista[middle - 1]:
                notfound = False
                print('{} found at {}'.format(c, middle + 1))
                break
            else:
                if c <= lista[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
        if notfound:
            print('{} not found'.format(c))
    count += 1
