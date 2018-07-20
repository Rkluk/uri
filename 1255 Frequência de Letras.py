u = int(input())
for c in range(u):
    dic = {}
    st = input().lower()
    for k in st:
        if 97 <= ord(k) <= 122:
            if k not in dic:
                dic[k] = 1
            else:
                dic[k] += 1
    b = ''
    for k in dic:
        if b == '' or dic[k] > b:
            b = dic[k]
    l = []
    for v in dic:
        if dic[v] < b:
            l.append(v)
    for v in l:
        del dic[v]
    l = []
    for v in dic:
        l.append(ord(v))
    l.sort()
    for v in range(len(l)):
        l[v] = chr(l[v])
    l = ''.join(l)
    print(l)
