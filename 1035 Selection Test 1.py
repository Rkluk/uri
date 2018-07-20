values = input().split()
A = int(values[0])
B = int(values[1])
C = int(values[2])
D = int(values[3])
c1 = bool(B > C)
c2 = bool(D > A)
c3 = bool((C + D) > (A + B))
c4 = bool(C > 0)
c5 = bool(D > 0)
c6 = A % 2
if c1 and c2 and c3 and c4 and c5 and c6 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
