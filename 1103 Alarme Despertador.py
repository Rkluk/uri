while True:
    a, b, aa, bb = [int(x) for x in input().split()]
    if a == b == aa == bb == 0:
        break
    if a > aa or a == aa and bb < b:
        print(((24 - a) * 60 - b) + (aa * 60 + bb))
    else:
        print(((aa - a) * 60) - (bb - b))
