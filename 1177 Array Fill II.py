user = int(input())
n = 0
for c in range(1000):
    print('N[{}] = {}'.format(c, n))
    n += 1
    if n == user:
        n = 0
