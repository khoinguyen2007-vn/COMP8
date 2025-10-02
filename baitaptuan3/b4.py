m,n = map(int,input().split())
k = format(m/n,'.0f')
if int(k) > m/n:
    print(int(k)-1)
else: 
    print(k)