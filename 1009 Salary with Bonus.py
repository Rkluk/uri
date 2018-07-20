name = str(input())
fsalary = float(input())
sold = float(input())
fsalary = round(fsalary, 1)
sold = round(sold, 1)
total = fsalary + sold * 0.15
print('TOTAL = R$ {:.2f}'.format(total))
