abc = input().split()
sort = sorted(abc, key=float)
a = round(float(sort[2]), 1)
b = round(float(sort[1]), 1)
c = round(float(sort[0]), 1)
p = bool(a >= (c + b))
if p:
    print('NAO FORMA TRIANGULO')
elif (a ** 2) == (b ** 2 + c ** 2):
    print('TRIANGULO RETANGULO')
elif (a ** 2) > (b ** 2 + c ** 2):
    print('TRIANGULO OBTUSANGULO')
elif (a ** 2) < (b ** 2 + c ** 2):
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b != c or a == c != b or b == c != a and not p:
    print('TRIANGULO ISOCELES')
