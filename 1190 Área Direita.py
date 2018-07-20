m = [[], [], [], [], [], [], [], [], [], [], [], []]
sm = input()
v = 0
for c in range(144):
    m[v].append(float(input()))
    if len(m[v]) == 12:
        v += 1
b1 = 0
b2 = 11
soma = 0
count = 0
for v in range(1, 11):
    soma += sum(m[v][b2:])
    count += len(m[v][b2:])
    if b1 == 0 and b2 > 7:
        b2 -= 1
    elif b2 == 7 and b1 != 2:
        b1 += 1
    if b1 == 2:
        b2 += 1
if sm == 'S':
    print('{:.1f}'.format(soma))
elif sm == 'M':
    print('{:.1f}'.format(soma / count))
