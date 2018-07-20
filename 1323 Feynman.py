while True:
       n, k = [int(input()), 0]
       if n == 0:
              break
       for c in range(n, 0, -1):
              k += c ** 2
       print(k)
