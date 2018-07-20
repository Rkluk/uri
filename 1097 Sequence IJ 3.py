j = [7, 6, 5]
i = 1
c = 0
while True:
    print('I={} J={}'.format(i, j[c]))
    if c == 2 and i == 9:
        break
    if c == 2:
        c = 0
        i += 2
        for n in range(0, 3):
            j[n] += 2
    else:
        c += 1
