n = int(input())
for c in range(n):
    st = input()
    l, dia = [0, 0]
    for c in st:
        if c == '<':
            l += 1
        elif c == '>' and l > 0:
            dia += 1
            l -= 1
    print(dia)
