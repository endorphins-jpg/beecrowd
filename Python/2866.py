casos_teste = int(input())

for i in range(casos_teste):
    cript = str(input())
    decript = ''
    for i in cript[::-1]:
        if i.islower():
            decript += i   
    print(decript)