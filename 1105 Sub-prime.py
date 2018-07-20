while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    banks, resp = [{}, 'S']
    banks_money = [int(x) for x in input().split()]
    for c in range(1, b + 1):
        banks[c] = banks_money[c - 1]
    for cases in range(1, n + 1):
        d, c, v = map(int, input().split())
        banks[d] -= v
        banks[c] += v
    for analysis in banks:
        if banks[analysis] < 0:
            resp = 'N'
            break
    print(resp)
