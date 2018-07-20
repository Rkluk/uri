t = int(input())
for testes in range(t):
    st1, st2 = input().split()
    soma = 0
    for c in range(len(st1)):
        if ord(st1[c]) == ord(st2[c]):
            pass
        elif ord(st1[c]) < ord(st2[c]):
            soma += ord(st2[c]) - ord(st1[c])
        else:
            soma += (123 - ord(st1[c])) + (ord(st2[c]) - 97)
    print(soma)
