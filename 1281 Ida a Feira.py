for casos in range(int(input())):
       dic, custo = [{}, 0]
       for produtos in range(int(input())):
              a, b = input().split()
              dic[a] = float(b)
       for compras in range(int(input())):
              prod, quant = input().split()
              custo += dic[prod] * int(quant)
       print('R$ {:.2f}'.format(custo))
