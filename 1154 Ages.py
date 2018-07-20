soma = 0
count = 0
while True:
    user = int(input())
    if user < 0:
        break
    soma += user
    count += 1
print('{:.2f}'.format(soma / count))
