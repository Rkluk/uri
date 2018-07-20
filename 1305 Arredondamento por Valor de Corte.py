while True:
    try:
        num = input()
        cutoff = float(input())
        if '.' in num and len(num[num.find('.'):]) > 1:
            pdec = '0'+(num[num.find('.'):])
            try:
                pint = int(num[:num.find('.')])
            except:
                pint = 0
            while len(pdec) < len(str(cutoff)):
                pdec += '9'
            if float(pdec) >= cutoff:
                result = pint + 1
            else:
                result = pint
        else:
            if '.' not in num:
                result = int(num)
            else:
                result = int(num[:num.find('.')])
        print(result)
    except EOFError:
        break
