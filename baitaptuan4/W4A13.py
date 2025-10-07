def sum(x):
    tong = 1
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            if i * i != x:
                tong += i + x // i
            else:
                tong += i
    return tong
a,b = map(int, input().split())
if sum(a) == b and sum(b) == a:
    print("true")
else:
    print("false")
