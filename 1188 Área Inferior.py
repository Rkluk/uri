m = [[], [], [], [], [], [], [], [], [], [], [], []]
sm = input()
v = 0
for c in range(144):
    m[v].append(float(input()))
    if len(m[v]) == 12:
        v += 1
b1 = 5
b2 = 7
soma = 0
count = 0
for v in range(7, 12):
    soma += sum(m[v][b1:b2])
    count += len(m[v][b1:b2])
    b1 -= 1
    b2 += 1
if sm == 'S':
    print('{:.1f}'.format(soma))
elif sm == 'M':
    print('{:.1f}'.format(soma / count))
