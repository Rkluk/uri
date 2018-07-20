a = int(input())
c, b = [int(x) for x in input().split()]
d, e = [int(x) for x in input().split()]
k = 'possivel' if c <= a <= b and d <= a <= e else 'impossivel'
print(k)
