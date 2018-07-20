abc = input().split()
A = float(abc[0])
B = float(abc[1])
C = float(abc[2])
a = (A * C) / 2
b = 3.14159 * C ** 2
c = (C * (A + B)) / 2
d = B ** 2
e = A * B
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(a, b, c, d, e))
