k, l = [0, 0]
while True:
    try:
        nome = input();k += 1; l += int(input())
    except EOFError:
        break
print('{:.1f}'.format(l / k))
