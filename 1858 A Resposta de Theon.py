n = int(input())
people = input().split()
b = ''
for x in range(n):
    if b == '' or int(people[x]) < b:
        b = int(people[x])
        v = x + 1
print(v)
