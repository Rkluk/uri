u = int(input())
for x in range(u):
    string = input().strip().split()
    codigo = ''
    for c in string:
        if 97 <= ord(c[0]) <= 122:
            codigo += c[0]
    print(codigo)
