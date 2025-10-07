def check(x):
    if (x**0.5) % 1 == 0:
        return True
    return False
dem = 0
n = int(input())
for i in range(1, n + 1):
    if check(i):
        dem += 1
        print(i, end=' ')
if dem == 0:
    print("no number")