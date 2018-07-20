casos = 1
while True:
    try:
        n, f, m, p, cal = [int(input()), 0,0, 0, input().split()]
        for c in range(0, len(cal), 2):
            if int(cal[c]) == n:
                p += 1
                if cal[c + 1] == 'F':
                    f += 1
                elif cal[c + 1] == 'M':
                    m += 1
        if casos > 1:
            print()
        print('Caso {}:\nPares Iguais: {}\nF: {}\nM: {}'.format(casos, p, f, m))
        casos += 1
    except EOFError:
        break
