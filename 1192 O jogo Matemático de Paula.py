for c in range(int(input())):
    n1, l, n2 = list(input())
    n1, n2 = [int(n1), int(n2)]
    if n1 == n2:
        print(n1 * n2)
    elif 97 <= ord(l) <= 122:
        print(n1 + n2)
    else:
        print(n2 - n1)
