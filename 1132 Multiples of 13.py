x = int(input())
y = int(input())
b = [x, y]
b.sort()
x = b[0]
y = b[1]
soma = 0
for c in range(x, y + 1):
    if c % 13 != 0:
        soma += c
print(soma)
