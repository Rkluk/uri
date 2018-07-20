user = int(input())
results = []
for textos in range(user):
    text = input()
    lista = list(text)
    for b in range(len(lista)):
        cha = lista[b]
        if (97 <= ord(cha) <= 122) or (65 <= ord(cha) <= 90):
            lista[b] = chr(ord(cha) + 3)
    text = ''.join(lista)
    text = text[::-1]
    lista = list(text)
    for b in range((len(lista)//2), len(lista)):
        lista[b] = chr(ord(lista[b]) - 1)
    text = ''.join(lista)
    results.append(text)
for imp in results:
    print(imp)
