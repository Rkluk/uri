x, y = [int(v) for v in input().split()]
count = 1
for c in range(1, y+1):
    if count < x:
        print(c, end=' ')
    elif count == x:
        count = 0
        print(c)
    count += 1
