lista = []
count = 0
med = 0
while count != 2:
    nota = float(input())
    if 0 <= nota <= 10:
        count += 1
        med += nota
    else:
        lista.append('nota invalida')
lista.append('media = {}'.format(med / 2))
for b in lista:
    print(b)
