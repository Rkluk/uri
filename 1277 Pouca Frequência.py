def faltas(x, y):
    v = ''
    a = 0
    j = list(y)
    o = y.count('M')
    for c in range(o):
        j.remove('M')
    y = ''.join(j)
    for c in y:
        if c == 'A':
            a += 1
    b = a / len(y) if len(y) > 0 else 0
    if (b * 100) > 25:
        v = x
    return v
n = int(input())
for x in range(n):
    est = int(input())
    alunos = input().split()
    freq = input().split()
    lista = []
    for k in range(est):
        lista.append(faltas(alunos[k], freq[k]))
    k = list(lista)
    h = 0
    for c in range(len(k)):
        if len(k[c]) == 0:
            lista.pop(c - h)
            h += 1
    if len(lista) > 0:
        for v in range(len(lista)):
            if v == len(lista) - 1:
                print(lista[v])
            else:
                print(lista[v], end=' ')
    else:
        print('')
