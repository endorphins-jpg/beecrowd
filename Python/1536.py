qt = int(input())

for i in range(qt):
  a_casa, b_fora = input().split(' x ')
  b_casa, a_fora = input().split(' x ')
  a_casa = int(a_casa)
  a_fora = int(a_fora)
  b_casa = int(b_casa)
  b_fora = int(b_fora)

  A = a_casa + a_fora
  B = b_casa + b_fora

  if A > B:
    print("Time 1")
  elif B > A:
    print("Time 2")
  else:
    if a_fora > b_fora:
      print("Time 1")
    elif b_fora > a_fora:
      print("Time 2")
    else:
      print("Penaltis")