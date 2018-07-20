u = int(input())
for c in range(u):
    st = list(input())
    ind = int(input())
    fn = ''
    for v in st:
        if (ord(v) - ind) < 65:
            fn += chr(91 - (65 - (ord(v) - ind)))
        else:
            fn += chr(ord(v) - ind)
    print(fn)
