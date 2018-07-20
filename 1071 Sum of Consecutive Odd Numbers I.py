a = 0
b = 0
soma = 0
for c in range(0,2):
    user = int(input())
    if a == 0 or user > a:
        a = user
    if b == 0 or user < b:
        b = user
for n in range(b + 1, a):
    if n % 2 != 0:
        soma += n
print(soma)
