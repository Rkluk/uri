while True:
    try:
        s1 = input()
        s2 = input()
        k = ''
        v = 0
        for finder in s1:
            if finder in s2 and len(k) == 0:
                k += finder
            elif str(k + finder) in s2:
                k += finder
            elif str(k + finder) not in s2 and finder in s2:
                b = str(k)
                for c in range(len(k)):
                    k = k[c:]
                    if k + finder in s2 and k != '':
                        po = True
                        break
                    else:
                        po = False
                if not po:
                    k = str(b)
                    v = len(k) if len(k) > v else v
                    k = ''
                    k += finder
                else:
                    k += finder
            else:
                v = len(k) if len(k) > v else v
                k = ''
        if len(k) > 0 and len(k) > v:
            v = len(k)
        print(v)
    except EOFError:
        break
