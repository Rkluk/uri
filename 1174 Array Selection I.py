lista = []
for user in range(100):
    num = float(input())
    if num <= 10:
        lista.append('A[{}] = {:.1f}'.format(user, num))
for imp in lista:
    print(imp)
