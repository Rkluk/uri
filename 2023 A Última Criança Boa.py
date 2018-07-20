def bubble(x):
    ready = False
    while not ready:
        mud = 0
        for c in range(len(x)):
            if c != len(x) - 1 and sorted([str(x[c]).lower(), str(x[c + 1]).lower()]) != [x[c].lower(), x[c + 1].lower()]:
                k = x[c]
                x[c] = x[c + 1]
                x[c + 1] = k
                mud = 1
        if mud == 0:
            ready = True
    return lista[-1]
lista = []
while True:
    try:
        lista.append(input())
    except EOFError:
        x = bubble(lista)
        break
print(x)
