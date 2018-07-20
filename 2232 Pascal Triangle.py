for c in range(int(input())):
    triangle, s, k = [[[1]], int(input()), 0]
    for x in range(1, s):
        temp = []
        for z in range(x + 1):
            if z == 0:
                temp.append(1)
            else:
                try:
                    temp.append(triangle[abs(x - 1)][abs(z - 1)] + triangle[abs(x - 1)][z])
                except:
                    temp.append(1)
        triangle.append(temp)
    for x in triangle:
        k += sum(x)
    print(k)
