p, j1, j2, r, a = map(int, input().split())
if r == a == 0:
    if p == 1:
        w = 1 if (j1 + j2) % 2 == 0 else 2
    else:
        w = 1 if (j1 + j2) % 2 == 1 else 2
elif r == a == 1:
    w = 2
elif r == 1 and a == 0:
    w = 1
elif r == 0 and a == 1:
    w = 1
print('Jogador {} ganha!'.format(w))
