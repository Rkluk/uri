dic = {'pedrapedra' : 'Sem ganhador', 'papelpapel' :  'Ambos venceram', 'ataqueataque' : 'Aniquilacao mutua', 'pedrapapel' : 'Jogador 1 venceu', 'papelpedra' : 'Jogador 2 venceu', 'ataquepedra' : 'Jogador 1 venceu', 'pedraataque' : 'Jogador 2 venceu', 'ataquepapel' : 'Jogador 1 venceu', 'papelataque' : 'Jogador 2 venceu'}
n = int(input())
for testes in range(n):
    jog1 = input()
    jog2 = input()
    print(dic[jog1 + jog2])
