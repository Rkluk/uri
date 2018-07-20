lista = []
for user in range(10):
    num = int(input())
    if num > 0:
        lista.append('X[{}] = {}'.format(user, num))
    else:
        lista.append('X[{}] = 1'.format(user))
for imp in lista:
    print(imp)
