A, B, C = input() .split()
A = float(A)
B = float(B)
C = float(C)

area_triangulo = (A * C)/2
area_circulo = 3.14159 * C ** 2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))