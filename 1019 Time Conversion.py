s = int(input())
m = s // 60
s %= 60
h = m // 60
m %= 60
print('{}:{}:{}'.format(h, m, s))
