h = 0
dic = {}
for c in range(65, 91):
    dic[chr(c)] = h
    h += 1
u = int(input())
for c in range(u):
    num = int(input())
    m = []
    soma = 0
    for v in range(num):
        m.append(list(input()))
    for v in range(num):
        for b in range(len(m[0])):
            soma += dic[m[v][b]] + v + b
    print(soma)
