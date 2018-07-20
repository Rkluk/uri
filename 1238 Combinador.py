u = int(input())
for c in range(u):
    a, b = input().split()
    c = ''
    if len(a) > len(b):
        for v in range(len(b)):
            c += a[v]
            c += b[v]
        c += a[len(b):]
    else:
        for v in range(len(a)):
            c += a[v]
            c += b[v]
        c += b[len(a):]
    print(c)
