def kt(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False    
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
sum = 0
a , b = map(int, input().split())
for so in range(a, b + 1):
    if kt(so):
        sum += so
print(sum)