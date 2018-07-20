while True:
    try:
        s1 = input()
        s2 = input()
        k = ''
        num = []
        for c in s1:
            if k + c in s2:
                k += c
            else:
                num.append(len(k))
                b = str(k)
                for x in range(len(k)):
                    if k[x:] + c in s2:
                        k = k[x:] + c
                        break
                if k == b:
                    k = ''
        if len(k) > 0:
            num.append(len(k))
        num.sort()
        print(num[len(num) - 1])
    except EOFError:
        break
