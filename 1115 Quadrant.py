lista = []
while True:
    x, y = [int(z) for z in input().split()]
    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        lista.append('primeiro')
    elif x < 0 and y > 0:
        lista.append('segundo')
    elif x < 0 and y < 0:
        lista.append('terceiro')
    elif x > 0 and y < 0:
        lista.append('quarto')
for b in lista:
    print(b)
