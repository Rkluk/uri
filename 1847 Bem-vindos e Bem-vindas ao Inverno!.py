a, b, c = [int(x) for x in input().split()]
if (a > b < c) or (a == b < c) or (a > b == c) or ((a > b > c) and ((a - b) > (b - c)) or ((a < b < c)) and ((b - a) <= (c - b))):
    print(':)')
else:
    print(':(')
