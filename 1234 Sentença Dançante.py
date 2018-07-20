while True:
    try:
        p = ''
        k = 0
        user = input()
        for c in user:
            if c != ' ':
                if k == 0:
                    p += c.upper()
                    k = 1
                elif k == 1:
                    p += c.lower()
                    k = 0
            else:
                p += c
        print(p)
    except EOFError:
        break
