from math import sqrt
xy1 = input().split()
xy2 = input().split()
x1 = round(float(xy1[0]), 1)
y1 = round(float(xy1[1]), 1)
x2 = round(float(xy2[0]), 1)
y2 = round(float(xy2[1]), 1)
distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('%.4f' %distance)
