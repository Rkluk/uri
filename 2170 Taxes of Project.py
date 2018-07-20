p = 1
while True:
    try:
        x, y = [float(x) for x in input().split()]
        print('Projeto {}:\nPercentual dos juros da aplicacao: {:.2f} %'.format(p, (abs(x - y) / x) * 100))
        print()
        p += 1
    except EOFError:
        break
