while True:
    try:
        u = list(input())
        b = 0
        k = 0
        for c in range(len(u)):
            if u[c] == '_' and k == 0:
                u[c] = '<i>'
                k = 1
            elif u[c] == '*' and b == 0:
                u[c] = '<b>'
                b = 1
            elif u[c] == '_' and k == 1:
                u[c] = '</i>'
                k = 0
            elif u[c] == '*' and b == 1:
                u[c] = '</b>'
                b = 0
        u = ''.join(u)
        print(u)
    except EOFError:
        break
