while True:
    a, b = [int(x) for x in input().split()]
    if a == b == 0:
        break
    a, b, v1, k = [list(str(a)), list(str(b)), 0, 0] if a > b else [list(str(b)), list(str(a)), 0, 0]
    a.reverse()
    b.reverse()
    for c in a:
        v1, k = [v1 + 1, 1] if int(c) + int(b[0]) + k > 9 else [v1, 0]
        b.pop(0)
        b = [0] if len(b) == 0 else b
    if v1 == 0:
        print('No carry operation.')
    elif v1 == 1:
        print('1 carry operation.')
    else:
        print('{} carry operations.'.format(v1))
