while True:
    try:
        rw = input()
        proc = int(input())
        cic = 0
        p = int(proc)
        for c in rw:
            if c == 'R':
                p -= 1
                if p == 0:
                    cic += 1
                    p = int(proc)
            elif c == 'W':
                cic += 1
                if p < proc:
                    p = int(proc)
                    cic += 1
        if proc > p:
            cic += 1
        print(cic)
    except EOFError:
        break
