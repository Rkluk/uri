u = int(input())
for c in range(u):
    a, b = input().split()
    k = len(b)
    a = a[::-1]
    b = b[::-1]
    if a[:k] == b:
        print('encaixa')
    else:
        print('nao encaixa')
