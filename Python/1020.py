dias = int(input())
A = int(dias/365)
M = int((dias%365)/30)
D = int((dias%365)%30)

print(A,'ano(s)')
print(M, 'mes(es)')
print(D, 'dia(s)')