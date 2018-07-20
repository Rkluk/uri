c = 3
v = 2
soma = 1
while True:
    soma += c/v
    c += 2
    v += v
    if c > 39:
        break
print('{:.2f}'.format(soma))
