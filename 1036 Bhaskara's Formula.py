from math import sqrt
num = input().split()
a = float(num[0])
b = float(num[1])
c = float(num[2])
delta = (b ** 2) - (4 * a * c)
if a != 0 and delta >= 0:
    r1 = ((-1 * b) + sqrt(delta)) / (2 * a)
    r2 = ((-1 * b) - sqrt(delta)) / (2 * a)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(r1, r2))
else:
    print('Impossivel calcular')
