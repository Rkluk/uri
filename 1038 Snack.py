xy = input().split()
x = int(xy[0])
y = int(xy[1])
if x == 1:
    total = y * 4
elif x == 2:
    total = y * 4.5
elif x == 3:
    total = y * 5
elif x == 4:
    total = y * 2
elif x == 5:
    total = y * 1.5
print('Total: R$ %.2f' %total)
