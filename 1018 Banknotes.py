money1 = int(input())
n100 = money1 // 100
money = money1 % 100
n50 = money // 50
money %= 50
n20 = money // 20
money %= 20
n10 = money // 10
money %= 10
n5 = money // 5
money %= 5
n2 = money // 2
money %= 2
n1 = int(money / 1)
print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00'
      '\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'
      .format(money1, n100, n50, n20, n10, n5, n2, n1))
