while True:
    try:
        exp = input()
        count = 0
        for c in exp:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count == -1:
                break
        if count == 0:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break
