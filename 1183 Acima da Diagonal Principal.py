m = [[], [], [], [], [], [], [], [], [], [], [], []]
v = 0
sm = input().upper()
for c in range(144):
    m[v].append(float(input()))
    if len(m[v]) == 12:
        v += 1
soma = 0
b = 1
count = 0
for c in m:
    soma += sum(c[b:])
    count += len(c[b:])
    b += 1
if sm == 'S':
    print('{:.1f}'.format(soma))
elif sm == 'M':
    print('{:.1f}'.format(soma / count))
