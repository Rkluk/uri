while True:
    try:
        user = input()
        if user == '':
            print('error')
        else:
            if 'o' in user:
                user = user.replace('o', '0')
            if 'O' in user:
                user = user.replace('O', '0')
            if 'l' in user:
                user = user.replace('l', '1')
            user = list(user)
            for c in range(len(user)):
                if ',' in user:
                    user.remove(',')
                if ' ' in user:
                    user.remove(' ')
            user = ''.join(user)
            try:
                if 2147483647 >= int(user) >= 0:
                    print(int(user))
                else:
                    print('error')
            except:
                print('error')
    except EOFError:
        break
