n = int(input())
for testes in range(n):
    k = int(input())
    idioma = ''
    for c in range(k):
        user = input()
        if idioma == '':
            idioma = user
        elif user != idioma:
            idioma = 'ingles'
    print(idioma)
