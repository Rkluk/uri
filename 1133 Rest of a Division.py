x = int(input())
y = int(input())
b = [x, y]
b.sort()
x = b[0]
y = b[1]
for c in range(x + 1, y):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
