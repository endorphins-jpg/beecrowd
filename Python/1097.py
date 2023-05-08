i = 1
j = 7
loop_j = 7

while i <= 9:
    for x in range(3):
        print(f'I={i} J={loop_j}')
        loop_j-=1
    count=+1
    j+=2*count
    loop_j = j
    i+=2