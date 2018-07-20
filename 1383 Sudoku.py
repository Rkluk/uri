inst = 1
ver = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for testes in range(int(input())):
    sud, lin, col, quad, veri = [[], [], [], [], False]
    for montar in range(9):
        sud.append([int(num) for num in input().split()])
    for linhas in sud:
        lin.append(sorted(linhas))
    for v in lin:
        if v != ver:
            veri = True
            break
    if not veri:
        for num in range(9):
            col.append([k[num] for k in sud])
            col[num].sort()
    for v in col:
        if v != ver:
            veri = True
            break
    if not veri:
        k, n, j = [0, 0, 0]
        for num in range(3):
            for quads in range(3):
                quad.append([])
                for colu in range(3):
                    quad[j] += sud[colu + n][k:k + 3]
                k = k + 3 if k < 4 else 0
                j += 1
            n += 3
    for check in quad:
        check.sort()
        if check != ver:
            veri = True
            break
    st = 'Instancia {}\nNAO' if veri else 'Instancia {}\nSIM'
    print(st.format(inst))
    print()
    inst += 1
                
