salario = float(input())

if 0 <= salario <= 2000:
    print('Isento')
elif 2000.01 <= salario <= 3000:
    salario -= 2000
    print('R$ {:.2f}'.format(salario * 0.08))
elif 3000.01 <= salario <= 4500:
    salario -= 3000
    print('R$ {:.2f}'.format((salario * 0.18) + 80))
elif salario >= 4500.01:
    salario -= 4500
    print('R$ {:.2f}'.format((salario * 0.28) + 350))