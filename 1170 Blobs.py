for c in range(int(input())):
    count, peso = [0, float(input())]
    while peso > 1:
        peso /= 2
        count += 1
    print(count, 'dias')
