while True:
    try:
        v = float(input())
        d = float(input())
        print('ALTURA = {:.2f}\nAREA = {:.2f}'.format(v / ((d / 2) ** 2 * 3.14), (d / 2) ** 2 * 3.14))
    except EOFError:
        break
