while True:
    try:
        n, l, c = [int(x) for x in input().split()]
        text = input()
        t1 = text.split()
        t2 = ''
        numl = 0
        count = 0
        p = 0
        for x in text:
            t2 += x
            if x == ' ':
                count += 1
                k = len(t2)
                j = len(t1[count])
                if k + j > c or k == c:
                    numl += 1
                    t2 = ''
                p = 1
            if count == n - 1 and p == 0:
                numl += 1
                break
            p = 0
        pag = numl // l if numl % l == 0 else numl // l + 1
        print(pag)
    except EOFError:
        break
