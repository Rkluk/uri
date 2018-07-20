salary = float(input())
salary = round(salary, 2)
if salary <= 2000:
    taxe = 'Isento'
    print(taxe)
elif 2000 < salary <= 3000:
    taxe = ((salary - 2000) * 0.08)
    print('R$ {:.2f}'.format(taxe))
elif 3000 < salary <= 4500:
    taxe = ((salary - 3000) * 0.18 + (1000 * 0.08))
    print('R$ {:.2f}'.format(taxe))
elif 4500 < salary:
    taxe = ((salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08))
    print('R$ {:.2f}'.format(taxe))
