lista = []
while True:
    user = int(input())
    if user == 0:
        break
    soma = 0
    if user % 2 == 1:
        user += 1
    for c in range(user, user + 10, 2):
        soma += c
    lista.append(soma)
for c in lista:
    print(c)
