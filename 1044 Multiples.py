n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
mult = n2 % n1
mult2 = n1 % n2
if mult == 0 or mult2 == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
