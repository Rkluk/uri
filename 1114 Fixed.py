lista = []
while True:
    user = int(input())
    if user != 2002:
        lista.append('Senha Invalida')
    else:
        lista.append('Acesso Permitido')
        break
for b in lista:
    print(b)
