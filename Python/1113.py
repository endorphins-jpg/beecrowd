num_1 = 0
num_2 = 1

while num_1 != num_2:
    num_1, num_2 = map(int, input().split())
    if num_1 > num_2:
        print('Decrescente')
    elif num_1 < num_2:
        print('Crescente')
