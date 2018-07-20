while True:
    n = int(input())
    if n == 0:
        break
    bits = input().split();x, y = [0, 0]
    for c in bits:
        if c == '0':
            x += 1
        else:
            y += 1
    print('Mary won {} times and John won {} times'.format(x, y))
