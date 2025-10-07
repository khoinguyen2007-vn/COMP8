n = int(input())
for i in range(n//2,-1,-1):
    if (i*(i+1))/2 < n:
        print(i)
        break