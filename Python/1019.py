N = int(input())
h = int(N/3600)
m = int((N%3600)/60)
s = int((N%3600)%60)

print('{}:{}:{}'.format(h,m,s))