n = int(input())
for x in range(n):
    bro = input()
    erros = 0
    if len(bro) == 5:
        num = 3
    else:
        for c in range(3):
            if bro[c] != 'one'[c]:
                erros += 1
        if erros <= 1:
            num = 1
        else:
            num = 2
    print(num)
