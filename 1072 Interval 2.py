user = int(input())
count_in = 0
count_out = 0
for c in range(0, user):
    user2 = int(input())
    if 10 <= user2 <= 20:
        count_in += 1
    else:
        count_out += 1
print('{} in\n{} out'.format(count_in, count_out))
