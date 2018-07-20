while True:
    n, pa, pb = [int(input()), 0, 0]
    if n == 0:
        break
    for c in range(n):
        a, b = map(int, input().split())
        if a > b:
            pa += 1
        elif b > a:
            pb += 1
    print(pa, pb)
