lista = []
user = int(input())
for c in range(user):
    num = int(input())
    soma = 0
    for v in range(1, num):
        if num % v == 0:
            soma += v
    if soma == num:
        lista.append('{} eh perfeito'.format(num))
    else:
        lista.append('{} nao eh perfeito'.format(num))
for b in lista:
    print(b)
