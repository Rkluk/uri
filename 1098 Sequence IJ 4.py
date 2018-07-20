i = 0
j = [1, 2, 3]
c = 0
while True:
    print('I={} J={}'.format(i, i + j[c]))
    if c == 2 and i == 2:
        break
    if c == 2:
        c = 0
        i += 0.2
        i = round(i, 1)
        if i == 1 or i == 2:
            i = round(i)
    else:
        c += 1
