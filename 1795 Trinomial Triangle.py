row, r = [[1], int(input())]
for c in range(r):
    row = [sum(t) for t in zip([0, 0] + row, [0] + row + [0], row + [0,0])]
print(sum(row))
