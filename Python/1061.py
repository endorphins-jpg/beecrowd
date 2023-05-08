dia_i = input().split()
hora_i, min_i, seg_i = map(int, input().split(' : '))

dia_f = input().split()
hora_f, min_f, seg_f = map(int, input().split(' : '))

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

dia_i = int(dia_i[-1])
dia_f = int(dia_f[-1])

seg = seg_f - seg_i
mi = min_f - min_i
hora = hora_f - hora_i
dia = dia_f - dia_i

if seg < 0:
    seg += 60
    mi -= 1

if mi < 0:
    mi += 60
    hora -= 1

if hora < 0:
    hora += 24
    dia -= 1

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{mi} minuto(s)")
print(f"{seg} segundo(s)")