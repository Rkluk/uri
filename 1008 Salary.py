number = int(input())
hours = int(input())
perhour = float(input())
perhour = round(perhour, 2)
salary = hours * perhour
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(number, salary))
