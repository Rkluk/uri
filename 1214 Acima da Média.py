for testes in range(int(input())):
       a = []
       a.append([int(x) for x in input().split()])
       tot, b = [sum(a[0][1:]) / a[0][0], 0]
       for c in a[0][1:]:
              b += 1 if c > tot else 0
       print('{:.3f}%'.format(b * 100 / len(a[0][1:])))
