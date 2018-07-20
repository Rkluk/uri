while True:
    user = input()
    try:
        if int(user) == 0:
            break
    except:
        a, b, c = [int(x) for x in user.split()]
    ar = a * b
    perc = 1 / (c / 100)
    tot = ar * perc
    tot = tot ** (1/2)
    k = str(tot)
    if '.' in k:
        l = k.find('.')
        k = k[:l]
        tot = int(k)
    print('{:.0f}'.format(tot))
