a, b = [int(x) for x in input().split()]
if b < 0 and a % b != 0:
    q = a // b + 1
else:
    q = a // b
r = a - (q * b)
print(q, r)
