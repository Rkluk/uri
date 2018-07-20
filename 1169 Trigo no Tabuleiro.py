for c in range(int(input())):
    g = 1
    for c in range(int(input())):
        g += g
    print(((g //12) // 1000), 'kg')
