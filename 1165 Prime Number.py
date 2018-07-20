lista = []
user = int(input())
for testes in range(user):
    num = int(input())
    count = 0
    for teste in range(1, num):
        if num % teste == 0:
            count += 1
    if count == 1:
        lista.append('{} eh primo'.format(num))
    else:
        lista.append('{} nao eh primo'.format(num))
for imp in lista:
    print(imp)
