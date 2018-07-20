user = int(input())
count = 0
while count != 6:
    if user % 2 == 1:
        print(user)
        count += 1
    user += 1
