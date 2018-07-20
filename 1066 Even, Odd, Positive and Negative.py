even = 0
odd = 0
positive = 0
negative = 0
for c in range(0, 5):
    user = int(input())
    if user % 2 == 0:
        even += 1
    else:
        odd += 1
    if user > 0:
        positive += 1
    if user < 0:
        negative += 1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)'
      '\n{} valor(es) negativo(s)'.format(even, odd, positive, negative))
