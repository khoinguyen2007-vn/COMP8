def check(n):
    list = [1,1]
    x = 1
    y = 1
    z = 0
    while z < n:
        z = x + y
        list.append(z)
        x = y
        y = z
    if n in list:
        return True
    return False
k = int(input())
for i in range(k,-1,-1):
    if check(i):
        print(i)
        break