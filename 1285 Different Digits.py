while True:
    try:
        n, m = [int(x) for x in input().split()]
        k = 0
        for c in range(n, m + 1):
            st, l , num = [str(c), [], True]
            for v in st:
                if v not in l:
                    l.append(v)
                else:
                    num = False
                    break
            if num:
                k += 1
        print(k)
    except EOFError:
        break
