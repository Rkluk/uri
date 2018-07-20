user  = int(input())
rabbit = 0
rat = 0
frog = 0
total = 0
for c in range(0, user):
    cod, ani = str(input()).split()
    cod = int(cod)
    if ani == 'C':
        rabbit += cod
    elif ani == 'R':
        rat += cod
    elif ani == 'S':
        frog += cod
    total += cod
prabbit = rabbit * 100 / total
prat = rat * 100 / total
pfrog = frog * 100 / total
print('Total: {} cobaias\n'
      'Total de coelhos: {}\n'
      'Total de ratos: {}\n'
      'Total de sapos: {}\n'
      'Percentual de coelhos: {:.2f} %\n'
      'Percentual de ratos: {:.2f} %\n'
      'Percentual de sapos: {:.2f} %'.format(total, rabbit, rat, frog, prabbit, prat, pfrog))
