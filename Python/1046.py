hora_inicial, hora_final = map(int, input().split())

if hora_final < hora_inicial or hora_final == hora_inicial:
    hora_final += 24

duracao = hora_final - hora_inicial

print('O JOGO DUROU {} HORA(S)'.format(duracao))