money = float(input())
money = round(money, 2)
n100 = money // 100
money %= 100
money = round(money, 2)
n50 = money // 50
money %= 50
money = round(money, 2)
n20 = money // 20
money %= 20
money = round(money, 2)
n10 = money // 10
money %= 10
money = round(money, 2)
n5 = money // 5
money %= 5
money = round(money, 2)
n2 = money // 2
money %= 2
money = round(money, 2)
n1 = money // 1
money %= 1
money = round(money, 2)
n05 = money // 0.5
money %= 0.5
money = round(money, 2)
n025 = money // 0.25
money %= 0.25
money = round(money, 2)
n010 = money // 0.10
money %= 0.10
money = round(money, 2)
n005 = money // 0.05
money %= 0.05
money = round(money, 2)
n001 = money / 0.01
print('NOTAS:\n'
    '{:.0f} nota(s) de R$ 100.00\n'
    '{:.0f} nota(s) de R$ 50.00\n'
    '{:.0f} nota(s) de R$ 20.00\n'
    '{:.0f} nota(s) de R$ 10.00\n'
    '{:.0f} nota(s) de R$ 5.00\n'
    '{:.0f} nota(s) de R$ 2.00\n'
    'MOEDAS:\n'
    '{:.0f} moeda(s) de R$ 1.00\n'
    '{:.0f} moeda(s) de R$ 0.50\n'
    '{:.0f} moeda(s) de R$ 0.25\n'
    '{:.0f} moeda(s) de R$ 0.10\n'
    '{:.0f} moeda(s) de R$ 0.05\n'
    '{:.0f} moeda(s) de R$ 0.01'
    .format(n100, n50, n20, n10, n5, n2, n1, n05, n025, n010, n005, n001))

