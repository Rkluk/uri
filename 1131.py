lista = []
inter = 0
gremio = 0
empate = 0
grenais = 0
while True:
    ng = 0
    grenais += 1
    vint, vgre = [int(x) for x in input().split()]
    if vint > vgre:
        inter += 1
    elif vgre > vint:
        gremio += 1
    else:
        empate += 1
    while ng != 1 and ng != 2:
        ng = int(input())
        lista.append('Novo grenal (1-sim 2-nao)')
    if ng == 2:
        break
for b in lista:
    print(b)
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}'.format(grenais, inter, gremio, empate))
if inter > gremio:
      print('Inter venceu mais')
elif gremio > inter:
      print('Gremio venceu mais')
else:
      print('Nao houve vencedor')
