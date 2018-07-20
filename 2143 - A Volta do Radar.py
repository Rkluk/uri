while True:
       n = int(input())
       if n == 0:
              break
       for c in range(n):
              num = int(input())
              if num % 2 == 1:
                     print((num % 2) + (num - num % 2) * 2)
              else:
                     print(num * 2 - 2)

