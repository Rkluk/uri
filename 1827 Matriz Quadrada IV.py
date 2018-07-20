while True:
    try:
        n = int(input())
        m = []
        for c in range(n):
            l = []
            for v in range(n):
                l.append(0)
            m.append(l)
        j1 = n // 3
        j2 = n - (n // 3)
        for c in range(n):
            for v in range(n):
                if j1 <= c < j2 and j1 <= v < j2:
                    m[c][v] = 1
                elif c == v:
                    m[c][v] = 2
                elif c + v == n - 1:
                    m[c][v] = 3
                if c == v and c + v == n - 1:
                    m[c][v] = 4
        for c in range(n):
            for v in range(n):
                if v == n - 1:
                    print(m[c][v])
                else:
                    print(m[c][v], end='')
        print()
    except EOFError:
        break
