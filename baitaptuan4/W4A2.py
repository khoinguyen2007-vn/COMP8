def ktnt(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i=5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True
n= int(input())
if ktnt(n):
    print("TRUE")
else:
    print("FALSE")