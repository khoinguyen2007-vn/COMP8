def check(x):
    dem = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = x*3 + 1
        dem+=1
    return dem
max = 0
res = 0
n = int(input())
for i in range(1,n+1):
    if check(i) > max:
        max = check(i)
        res = i
print(res," ",max+1)