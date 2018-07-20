dic = {'1' : 2, '2' : 5, '3' : 5, '4' : 4, '5' : 5, '6' : 6, '7' : 3, '8' : 7, '9' : 6, '0' : 6}
user = int(input())
results = []
for c in range(user):
    num = list(input())
    soma = 0
    for c in num:
        soma += dic[c]
    results.append(soma)
for c in results:
    print(c, 'leds')
