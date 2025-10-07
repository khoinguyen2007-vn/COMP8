a,b = map(int,input().split())
for i in range(b//2,-1,-1):
    for j in range(b//4,-1,-1):
        if i*2 + j*4 == b and i + j == a:
            print(i," ",j)
            exit()
print("invalid") 