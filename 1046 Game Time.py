start, end = input().split()
start = int(start)
end = int(end)
if start < end:
    print('O JOGO DUROU {} HORA(S)'.format(end - start))
elif end < start:
    soma = (24 - start) + end
    print('O JOGO DUROU {} HORA(S)'.format(soma))
else:
    print('O JOGO DUROU 24 HORA(S)')
