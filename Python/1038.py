x = input() .split()
cod_item = int(x[0])
quant_item = int(x[1])

if cod_item == 1:
  preco_item= float(quant_item * 4.00)
  print('Total: R$ {:.2f}'.format(preco_item))
elif cod_item == 2:
  preco_item= float(quant_item * 4.50)
  print('Total: R$ {:.2f}'.format(preco_item))
elif cod_item == 3:
  preco_item= float(quant_item * 5.00)
  print('Total: R$ {:.2f}'.format(preco_item))
elif cod_item == 4:
  preco_item= float(quant_item * 2.00)
  print('Total: R$ {:.2f}'.format(preco_item))
elif cod_item == 5:
  preco_item= float(quant_item * 1.50)
  print('Total: R$ {:.2f}'.format(preco_item))