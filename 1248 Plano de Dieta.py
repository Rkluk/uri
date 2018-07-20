u = int(input())
for c in range(u):
    dieta= input()
    cafe= input()
    almoco = input()
    ldieta = []
    cheater = False
    for v in dieta:
        if ord(v) not in ldieta:
            ldieta.append(ord(v))
    lcafe = []
    for v in cafe:
        lcafe.append(ord(v))
    lalmoco = []
    for v in almoco:
        lalmoco.append(ord(v))
    ldieta.sort()
    for v in lcafe:
        if v in ldieta:
            for k in range(len(ldieta)):
                if ldieta[k] == v:
                    ldieta.pop(k)
                    break
        else:
            cheater = True
            break
    if not cheater:
        for v in lalmoco:
            if v in ldieta:
                for k in range(len(ldieta)):
                    if ldieta[k] == v:
                        ldieta.pop(k)
                        break
            else:
                cheater = True
                break
    if cheater:
        print('CHEATER')
    elif len(ldieta) > 0:
        for v in range(len(ldieta)):
            if v == (len(ldieta) - 1):
                print(chr(ldieta[v]))
            else:
                print(chr(ldieta[v]), end='')
    else:
        print('')
