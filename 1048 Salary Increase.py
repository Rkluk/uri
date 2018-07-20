salary = float(input())
salary = round(salary, 2)
if 0 <= salary <= 400:
    newsalary = 0.15
    percentual = '15 %'
elif 400 < salary <= 800:
    newsalary = 0.12
    percentual = '12 %'
elif 800 < salary <= 1200:
    newsalary = 0.10
    percentual = '10 %'
elif 1200 < salary <= 2000:
    newsalary = 0.07
    percentual = '7 %'
elif 2000 < salary:
    newsalary = 0.04
    percentual = '4 %'
newsalary = newsalary * salary + salary
earned = newsalary - salary
print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'
      .format(newsalary, earned, percentual))
