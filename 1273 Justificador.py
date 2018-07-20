h = 0
while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for c in range(n):
        l.append(input())
    b = ''
    for c in l:
        if b == '' or len(c) > b:
            b = len(c)
    if h == 1:
        print('')
    for c in l:
        print('{:>{}}'.format(c, b))
    h = 1
