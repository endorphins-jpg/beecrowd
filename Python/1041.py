valores= input() .split()
x = float(valores[0])
y = float(valores[1])

if x == y == 0:
  print('Origem')
elif x != 0 and y == 0:
  print('Eixo X')
elif x == 0 and y != 0:
  print('Eixo Y')
elif x > 0 and y > 0:
  print('Q1')
elif x < 0 and y > 0:
  print('Q2')
elif x < 0 and y < 0:
  print('Q3')
elif x > 0 and y < 0:
  print('Q4')