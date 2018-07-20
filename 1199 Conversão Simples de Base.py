while True:
    num = input()
    if int(num, 16) < 0:
        break
    x = int(num, 16) if 'x' in num else str(hex(int(num)))[:2] + (str(hex(int(num)))[2:]).upper()
    print(x)
