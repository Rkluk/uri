par = []
impar = []
for user in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        n = 0
        for c in range(5):
            print('par[{}] = {}'.format(c, par[c]))
            n += 1
        par = []
    if len(impar) == 5:
        n = 0
        for c in range(5):
            print('impar[{}] = {}'.format(c, impar[c]))
            n += 1
        impar = []
v = 0
for k in impar:
    print('impar[{}] = {}'.format(v, k))
    v += 1
b = 0
for p in par:
    print('par[{}] = {}'.format(b, p))
    b += 1
