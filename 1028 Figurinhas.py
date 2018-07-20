from fractions import gcd
n = int(input())
for c in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))
