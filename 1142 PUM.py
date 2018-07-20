user = int(input())
v = -1
for g in range(-1, user -1):
    for c in range(v + 2, v + 5):
        print(c, end=' ')
        v += 1
    v += 1
    print('PUM')
