while True:
    n, d = [int(x) for x in input().split()]
    if n == d == 0:
        break
    presence, anwser = [{}, 'no']
    for alumni in range(n):
        presence[alumni] = 0
    for dinners in range(d):
        alumni = [int(x) for x in input().split()]
        for confirm in range(n):
            if alumni[confirm] == 1:
                presence[confirm] += 1
    for check in presence:
        if presence[check] == d:
            anwser = 'yes'
            break
    print(anwser)
