n, z, b = [int(input()), 0, 0]
for c in range(n):
    z += float(input())
    frutas = input().split()
    b += len(frutas)
    print('day {}: {} kg'.format(c + 1, len(frutas)))
print('{:.2f} kg by day\nR$ {:.2f} by day'.format(b / n, z / n))
