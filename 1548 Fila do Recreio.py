for casos in range(int(input())):
       alunos, notas, mudanca = [int(input()), [[int(nota) for nota in input().split()]][0], 0]
       lista = list(notas)
       lista.sort()
       lista.reverse()
       for fila in range(alunos):
              mudanca += 1 if notas[fila] == lista[fila] else 0
       print(mudanca)
