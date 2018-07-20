while True:
    sentenc = input().lower()
    if sentenc == '*':
        break
    sp = sentenc.split();k = '';taut = 'Y'
    for c in sp:
        if k == '':
            k = c[0]
        elif k != c[0]:
            taut = 'N'
            break
    print(taut)
