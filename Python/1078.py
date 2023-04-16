valor = int(input())

if 2 < valor < 1000:
    for i in range(1, 11):
        print('{} x {} = {}'.format(i, valor, i*valor))