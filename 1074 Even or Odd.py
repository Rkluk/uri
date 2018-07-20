user = int(input())
a = []
for c in range(0, user):
    user2 = int(input())
    if user2 == 0:
        a.append('NULL')
    elif user2 % 2 == 0 and user2 > 0:
        a.append('EVEN POSITIVE')
    elif user2 % 2 == 0 and user2 < 0:
        a.append('EVEN NEGATIVE')
    elif user2 % 2 == 1 and user2 > 0:
        a.append('ODD POSITIVE')
    elif user2 % 2 == 1 and user2 < 0:
        a.append('ODD NEGATIVE')
for n in range(0, user):
    print(a[n])
