m = [[], [], [], [], [], [], [], [], [], [], [], []]
sm = input()
v = 0
for c in range(144):
    m[v].append(float(input()))
    if len(m[v]) == 12:
        v += 1
b = 12
soma = 0
count = 0
for c in m:
    soma += sum(c[b:])
    count += len(c[b:])
    b -= 1
if sm == 'S':
    print('{:.1f}'.format(soma))
elif sm == 'M':
    print('{:.1f}'.format(soma / count))
