lista = [[], [], [], [], [], [], [], [], [], [], [], []]
count = 0
user = int(input())
u2 = input().upper()
for c in range(144):
    lista[count].append(float(input()))
    if len(lista[count]) == 12:
        count += 1
if u2 == 'S':
    print('{:.1f}'.format(sum(lista[user])))
elif u2 == 'M':
    print('{:.1f}'.format((sum(lista[user])) / 12))
