for c in range(int(input())):
    n, b = input().split()
    if b == 'bin':
        print('Case {}:\n{} dec\n{} hex'.format(c + 1, int(n, 2), str(hex(int(n, 2)))[2:]))
    elif b == 'dec':
        print('Case {}:\n{} hex\n{} bin'.format(c + 1, str(hex(int(n)))[2:], str(bin(int(n)))[2:]))
    else:
        print('Case {}:\n{} dec\n{} bin'.format(c + 1, int(n, 16), str(bin(int(n, 16)))[2:]))
    print()
