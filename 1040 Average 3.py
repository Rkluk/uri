notas = input().split()
n1 = float(notas[0])
n1 = round(n1, 1)
n2 = float(notas[1])
n2 = round(n2, 1)
n3 = float(notas[2])
n3 = round(n3, 1)
n4 = float(notas[3])
n4 = round(n4, 1)
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) /10
media = round(media, 1)
if media >= 7.0:
    print('Media: %.1f' %media)
    print('Aluno aprovado.')
elif 5 <= media <= 6.9:
    exame = float(input())
    print('Media: %.1f' %media)
    exame = round(exame, 1)
    print('Aluno em exame.')
    print('Nota do exame: %.1f'%exame)
    final = (exame + media) / 2
    final = round(final, 1)
    if final >= 5:
        print('Aluno aprovado.\nMedia final: %.1f' %final)
    else:
        print('Aluno reprovado.')
else:
    print('Media: %.1f' %media)
    print('Aluno reprovado.')
