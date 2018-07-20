i = 1
j = 7
while True:
    print('I={} J={}'.format(i, j))
    if i == 9 and j == 5:
        break
    if j == 7 or j == 6:
        j -= 1
    elif j == 5:
        i +=2
        j += 2
