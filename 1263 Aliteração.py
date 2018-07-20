while True:
    try:
        dic = {}
        string = input().lower().split()
        h = '0'
        for c in range(len(string)):
            if (string[c][0] + h) not in dic:
                dic[string[c][0] + h] = 1
            elif (string[c][0] + h) in dic and string[c - 1][0] != string[c][0]:
                h += '0'
                dic[string[c][0] + h] = 1
            else:
                dic[string[c][0] + h] += 1
        soma = 0
        for c in dic:
            if dic[c] > 1:
                soma += 1
        print(soma)
    except EOFError:
        break
