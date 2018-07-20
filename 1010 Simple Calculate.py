a = input().split()
b = input().split()
a0 = int(a[0])
b0 = int(b[0])
a2 = round(float(a[2]), 2)
b2 = round(float(b[2]), 2)
value = int(a[1]) * a2 + int(b[1]) * b2
print('VALOR A PAGAR: R$ {:.2f}'.format(value))
