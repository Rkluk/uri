while True:
    n = int(input())
    if n == 0:
        break
    for x in range(n):
        dic, k = [{0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E'}, '']
        resp =[int(x) for x in input().split()]
        for c in range(5):
            if resp[c] <= 127 and k == '':
                k = dic[c]
            elif resp[c] <= 127 and k != '':
                k = '*'
                break
        if k == '':
            k = '*'
        print(k)
