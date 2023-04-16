hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

total_minutos_inicial = hora_inicial * 60 + minuto_inicial
total_minutos_final = hora_final * 60 + minuto_final

if total_minutos_final <= total_minutos_inicial:
    total_minutos_final += 24 * 60

duracao_minutos = total_minutos_final - total_minutos_inicial
duracao_horas = duracao_minutos // 60
duracao_minutos = duracao_minutos % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_minutos))