def check(x):
    dem = 0
    if x == 1:
        return dem
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0 and i * i != x:
            if i % 2 == 0:
                dem += 1
            if (x // i) % 2 == 0:
                dem += 1
        elif i * i == x and i % 2 == 0:
            dem += 1
    return dem
n = int(input())
print(check(n))