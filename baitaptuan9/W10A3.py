def sum_of_num(x):
    res = 0
    while x != 0:
        res += (x % 10)**2
        x //= 10
    return res
try:
    check = True
    a = int(input())
    while sum_of_num(a) != 1:
        a = sum_of_num(a)
        if a == 4:
            print("No")
            check = False
            break
    if check:
        print("Yes")
except:
    print("Error")
    

    
