while True:
    try:
        n = int(input())
        dic = {}
        lista = []
        for c in range(n):
            carne, num = input().split()
            num = int(num)
            if num not in dic:
                dic[num] = carne
                lista.append(num)
            else:
                dic[num] += ' ' + carne
        lista.sort()
        for c in range(len(lista)):
            if c == len(lista) - 1:
                print(dic[lista[c]])
            else:
                print(dic[lista[c]], end=' ')
    except EOFError:
        break
