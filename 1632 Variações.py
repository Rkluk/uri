letras = [chr(x) for x in range(97, 123)]
letrasm = [chr(x) for x in range(65, 91)]
dic = {}
for x in range(26):
    dic[letras[x]] = 2
    dic[letrasm[x]] = 2
dic['a'] += 1
dic['A'] += 1
dic['e'] += 1
dic['E'] += 1
dic['i'] += 1
dic['I'] += 1
dic['o'] += 1
dic['O'] += 1
dic['s'] += 1
dic['S'] += 1
t = int(input())
for testes in range(t):
    s = input()
    soma = 1
    for c in s:
        soma *= dic[c]
    print(soma)
