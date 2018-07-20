soma = 0
user = int(input())
u2 = input().upper()
for c in range(144):
    num = float(input())
    if c == user:
        soma += num
        user += 12
if u2 == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/12))
