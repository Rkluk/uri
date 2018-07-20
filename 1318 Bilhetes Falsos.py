while True:
    n, m = [int(x) for x in input().split()]
    if n == m == 0:
        break
    dic, clone = [{}, 0]
    bilhetes = [int(x) for x in input().split()]
    for c in bilhetes:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    for c in dic:
        if dic[c] > 1:
            clone += 1
    print(clone)
