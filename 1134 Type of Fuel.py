a = 0
g = 0
d = 0
while True:
    user = int(input())
    if user == 1:
        a += 1
    elif user == 2:
        g += 1
    elif user == 3:
        d += 1
    elif user == 4:
        break
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(a, g, d))
