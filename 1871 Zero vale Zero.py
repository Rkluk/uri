while True:
    m, n = [int(x) for x in input().split()]
    if m == n == 0:
        break
    soma = m + n
    st = str(soma)
    l = list(st)
    k = 0
    for c in range(len(st)):
        if st[c] == '0':
            l.pop(c - k)
            k += 1
    l = ''.join(l)
    print(l)
