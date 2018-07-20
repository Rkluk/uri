"""from fractions import gcd
for c in range(int(input())):
       n, p = [int(input()), 'Prime']
       if n == 2:
              pass
       elif n % 2 == 0:
              p = 'Not Prime'
       else:
              for a in range(3, 50000, 2):
                     if gcd(a, n) != 1:
                            p = 'Not Prime'
                            break
       print(p)
"""
from gmpy2 import is_prime
for c in range(int(input())):
       if is_prime(int(input())):
              print('Prime')
       else:
              print('Not Prime')
