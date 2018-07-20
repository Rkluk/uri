user = int(input())
for c in range(1, user + 1):
    if c % 2 == 0:
        print('{}^2 = {}'.format(c, c ** 2))
