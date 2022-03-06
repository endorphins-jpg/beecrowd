sal = float(input())

if sal > 0 and sal <= 400.00:
    sp = sal * 0.15
    st = sp + sal
    print('Novo salario: {:.2f}'.format(st))
    print('Reajuste ganho: {:.2f}'.format(sp))
    print('Em percentual: 15 %')

elif sal <= 800.00:
    sp = sal * 0.12
    st = sp + sal
    print('Novo salario: {:.2f}'.format(st))
    print('Reajuste ganho: {:.2f}'.format(sp))
    print('Em percentual: 12 %')

elif sal <= 1200.00:
    sp = sal * 0.10
    st = sp + sal
    print('Novo salario: {:.2f}'.format(st))
    print('Reajuste ganho: {:.2f}'.format(sp))
    print('Em percentual: 10 %')

elif sal <= 2000.00:
    sp = sal * 0.07
    st = sp + sal
    print('Novo salario: {:.2f}'.format(st))
    print('Reajuste ganho: {:.2f}'.format(sp))
    print('Em percentual: 7 %')

elif sal > 2000.00:
    sp = sal * 0.04
    st = sp + sal
    print('Novo salario: {:.2f}'.format(st))
    print('Reajuste ganho: {:.2f}'.format(sp))
    print('Em percentual: 4 %')