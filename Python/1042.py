x = input() .split()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])

if x1 < x2 and x2 < x3:
  print(x1)
  print(x2)
  print(x3)
elif x1 < x3 and x3 < x2:
  print(x1)
  print(x3)
  print(x2)
elif x2 < x1 and x1 < x3:
  print(x2)
  print(x1)
  print(x3)
elif x2 < x3 and x3 < x1:
  print(x2)
  print(x3)
  print(x1)
elif x3 < x1 and x1 < x2:
  print(x3)
  print(x1)
  print(x2)
elif x3 < x2 and x2 < x1:
  print(x3)
  print(x2)
  print(x1)

print("")
print(x1)
print(x2)
print(x3)