list=[]
dem = 0
while True:
    n = int(input())
    list.append(n)
    if n == -1:
        break
    dem +=1
list.sort()
print(list[0]," ",list[dem-1])