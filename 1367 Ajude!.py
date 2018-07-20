while True:
    n = int(input())
    if n == 0:
        break
    dic = {}
    p = 0
    s = 0
    v = 0
    for x in range(n):
        prob, t, julg = input().split()
        t = int(t)
        if not (prob in dic and 'c' == dic[prob]):
            if julg == 'incorrect':
                dic[prob] = 20 if prob not in dic else dic[prob] + 20
            else:
                s += 1
                if prob in dic:
                    p += t + dic[prob]
                    dic[prob] = 'c'
                else:
                    p += t
    print(s, p)
