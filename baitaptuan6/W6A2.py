numbers = list(map(int,input().split()))
num = []
for i in numbers:
    if len(num) == 0:
        num.append(i)
    else:
        num.append(num[len(num)-1]+i)
print(num)
