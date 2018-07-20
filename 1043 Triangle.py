a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
p = bool(abs(a - b) < c < (a + b))
if p:
  print('Perimetro = %.1f' %(a + b + c))
else:
  trap = ((a + b) / 2 ) * c
  print('Area = %.1f' %trap)
