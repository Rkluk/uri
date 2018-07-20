media = 0
positive = 0
for c in range(0, 6):
    user = float(input())
    if user > 0:
        positive += 1
        media += user
media /= positive
print('{} valores positivos\n{:.1f}'.format(positive, media))
