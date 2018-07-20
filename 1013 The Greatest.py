x = input().split()
v = 0
for c in range(0, 3):
    if int(x[c]) > v:
        v = int(x[c])
print(v,'eh o maior')
