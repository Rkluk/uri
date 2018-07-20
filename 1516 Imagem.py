while True:
    n, m= [int(x) for x in input().split()]
    if n == m == 0:
        break
    mz = []
    for c in range(n):
        mz.append(input())
    a, b = [int(x) for x in input().split()]
    mz1 = []
    mz2 = []
    rl = a // n
    rc = b // m
    for c in range(n):
        st = ''
        for v in range(m):
            st += mz[c][v] * rc
        mz1.append(st)
    for x in mz1:
        for c in range(rl):
            mz2.append(x)
    for c in mz2:
        print(c)
    print('')
