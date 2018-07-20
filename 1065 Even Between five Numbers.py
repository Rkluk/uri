even = 0
for c in range(0, 5):
    user = int(input())
    if user % 2 == 0:
        even += 1
print('{} valores pares'.format(even))
