casos_teste = int(input())
for i in range(casos_teste):
    v_1, v_2, v_3 = input().split()
    print('{:.1f}'.format((float(v_1)*2 + float(v_2)*3 + float(v_3)*5)/10))
