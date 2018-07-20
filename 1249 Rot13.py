def converter(a):
    if 97 <= ord(a) <= 122:
        if (ord(a) - 13) < 97:
            b = chr((123 - (97 - (ord(a) - 13))))
        else:
            b = chr(ord(a) - 13)
    elif 65 <= ord(a) <= 90:
        if (ord(a) - 13) < 65:
            b = chr((91 - (65 - (ord(a) - 13))))
        else:
            b = chr(ord(a) - 13)
    else:
        b = a
    return b
while True:
    try:
        user = input()
        st = ''
        for c in user:
            st += converter(c)
        print(st)
    except EOFError:
        break
