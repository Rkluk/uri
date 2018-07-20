while True:
    try:
        u = int(input())
        b = list(map(int, input().split()))
        c = ''
        for v in b:
            if c == '':
                c = v
            elif v > c:
                c = v
        if c < 10:
            print(1)
        elif 10 <= c < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
