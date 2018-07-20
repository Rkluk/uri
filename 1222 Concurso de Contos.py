def analisador(limite, texto):
    linhas = []
    k = limite
    j = 0
    while True:
        try:
            palavras = texto[j:(texto[:limite].rfind(' ')) + 1] if texto[limite] != ' ' else texto[j:limite]
        except:
            palavras = texto[j:]
        j = texto[:limite - 1].rfind(' ') + 1 if palavras == texto[j:(texto[:limite - 1].rfind(' ')) + 1] else limite
        linhas.append(palavras)
        if palavras[::-1] == texto[-1:-1 * len(palavras) -1:-1]:
            break
        limite += k
    return len(linhas)
while True:
    try:
        n, l, c = [int(x) for x in input().split()]
        text = input()
        linhastot = analisador(c, text)
        pag = linhastot // l + 1 if linhastot % l != 0 else linhastot // l
        print(pag)
    except EOFError:
        break
