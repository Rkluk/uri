from math import floor
n = float(input())
if n >= 1:
    if floor(n) == n:
        r = 0
        m = False
        if 'e' not in str(n):
            while not 1 <= float(str(n)[:str(n).find('e')]) < 10:
                r -= 1 if m else 0
                n = float('{}E{}'.format(n, r))
                m = True
            r = int(str(r)[1:])
            print('+{:.4f}E+{:02d}'.format(n,-r))
        else:
            num = float(str(n)[:str(n).find('e')])
            r = int(str(n)[str(n).find('e') + 1:])
            print('+{:.4f}E+{:02d}'.format(num, r))
